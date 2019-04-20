'''
Utility for creating maps (one per island) that indicate, by region, which
huts have been visited.
'''

import folium

from hut import (
    north_island, south_island,
    regions_north, regions_south, unknown_region,
    unknown_place,
)
from merged import huts_enriched_with_trips

COOK_STRAIT = 'cook strait' # currently unused but that's ok :)
CENTER_OF_NORTH_ISLAND = 'center of north island'
CENTER_OF_SOUTH_ISLAND = 'center of south island'

def _base_map(focus=COOK_STRAIT):
    if focus == COOK_STRAIT:
        MAP_DEFAULT_LOCATION = [-41.4946 , 173.4930]
        ZOOM_START = 5
    elif focus == CENTER_OF_NORTH_ISLAND:
        MAP_DEFAULT_LOCATION = [-38.5472, 175.8032]
        ZOOM_START = 6
    elif focus == CENTER_OF_SOUTH_ISLAND:
        MAP_DEFAULT_LOCATION = [-43.8977, 170.6418]
        ZOOM_START = 6
    else:
        raise ValueError('unknown focus: {}'.format(focus))

    m = folium.Map(
        location=MAP_DEFAULT_LOCATION,
        zoom_start=ZOOM_START,
        control_scale=True, # show a scale bar e.g. "100 km" or "50 mi"
        # tiles='Stamen Terrain', # use a terrain-view for the underlying tileset
    )

    # Sometimes it is useful to enable lat/lng popups on the map. Do so by
    # uncommenting the following line:
    # m.add_child(folium.LatLngPopup())

    return m


ICON_HUT = 'home'
COLOR_HUT_VISITED = 'green'
COLOR_HUT_NOT_VISITED = 'orange'

VISITED = 'Visited'
NOT_VISITED = 'Not visited'


def maps(huts_with_trip_data):
    '''Returns a dict with island names for keys and maps for values. The maps
    depict the huts in a bunch of layers - one "visited" layer for every
    region and another "not visited" layer for every region.

    Hut names will be hyperlinks to the hut's url.
    The "place" will follow the hut name.
    For huts that have been visited, date strings and trip report links will
    follow the place name.
    '''
    island_maps = {
        north_island: _base_map(focus=CENTER_OF_NORTH_ISLAND),
        south_island: _base_map(focus=CENTER_OF_SOUTH_ISLAND),
    }

    regions_to_render = set(list(map(lambda h: h.region, huts_with_trip_data)))

    # By region
    region_groups = {}
    for i, m in island_maps.iteritems():
        region_groups[i] = {}

        if i == north_island:
            regions = regions_north
        elif i == south_island:
            regions = regions_south
        else:
            raise ValueError('unrecognized island: {}'.format(i))
        regions.append(unknown_region)

        for r in filter(lambda r: r in regions_to_render, regions):
            fg_visited_in_region = folium.FeatureGroup(
                name='{} - {}'.format(r, VISITED), show=False)
            fg_visited_in_region.add_to(m)

            fg_not_visited_in_region = folium.FeatureGroup(
                name='{} - {}'.format(r, NOT_VISITED), show=False)
            fg_not_visited_in_region.add_to(m)

            region_groups[i][r] = {
                VISITED: fg_visited_in_region,
                NOT_VISITED: fg_not_visited_in_region
            }

    for h in huts_with_trip_data:
        if h.visited:
            color = COLOR_HUT_VISITED
        else:
            color = COLOR_HUT_NOT_VISITED

        popup_str = h.render_name(html=True)
        if h.place != unknown_place:
            popup_str = u'{} <br/> ({})'.format(popup_str, h.place)
        if h.visited:
            popup_str = u'{}: <br/> visited {}'.format(popup_str, h.render_dates_visited(html=True))
        popup = folium.Popup(popup_str, max_width=150)

        marker = folium.Marker(
            location=(h.lat, h.lng),
            popup=popup,
            icon=folium.Icon(icon=ICON_HUT, color=color),
        )
        group = region_groups[h.island][h.region][VISITED if h.visited else NOT_VISITED]
        marker.add_to(group)

    # Layers for everybody!
    for m in island_maps.values():
        folium.LayerControl().add_to(m)

    return island_maps
