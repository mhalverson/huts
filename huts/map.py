'''
Exposes two maps (one per island) in the variable island_maps. The maps
indicate, by region, which huts have been visited.
'''

import folium

from hut import (
    north_island, south_island,
    regions_north, regions_south, unknown_region,
    unknown_place,
)
from merged import huts_enriched_with_visits

COOK_STRAIT = 'cook strait' # currently unused but thqt's ok :)
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

# Prepare the markers
ICON_HUT = 'home'
COLOR_HUT_VISITED = 'green'
COLOR_HUT_NOT_VISITED = 'orange'

VISITED = 'Visited'
NOT_VISITED = 'Not visited'


# Prepare the maps
island_maps = {
    north_island: _base_map(focus=CENTER_OF_NORTH_ISLAND),
    south_island: _base_map(focus=CENTER_OF_SOUTH_ISLAND),
}

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

    for r in regions:
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

    r = unknown_region
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

for h in huts_enriched_with_visits():
    if h.visited:
        color = COLOR_HUT_VISITED
    else:
        color = COLOR_HUT_NOT_VISITED

    popup_str = h.render_name_with_link()
    if h.place != unknown_place:
        popup_str = u'{} <br/> ({})'.format(popup_str, h.place)
    if h.visited:
        popup_str = u'{}: <br/> visited {}'.format(popup_str, h.render_dates_visited())
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
