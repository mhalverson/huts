'''
Defines the object representation of a Hut.
Exposes a list of all huts in New Zealand with all_huts().
Exposes lists of all places, all regions, all islands in definitive sort-orders.
'''

from collections import defaultdict
import json
import os.path

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
HUTS_FILE = os.path.join(BASE_DIR, 'data', 'DOC_Huts.geojson')

STATUS_OPEN = 'OPEN'


_regions_north = [
    u'Northland',
    u'Auckland',
    u'Coromandel',
    u'Waikato',
    u'Bay of Plenty',
    u'East Coast',
    u'Central North Island',
    u'Taranaki',
    u'Manawatu/Whanganui',
    u"Hawke's Bay",
    u'Wairarapa',
    u'Wellington/Kapiti',
]
_regions_south = [
    u'Nelson/Tasman',
    u'Marlborough',
    u'West Coast',
    u'Canterbury',
    u'Otago',
    u'Fiordland',
    u'Southland',
]
_regions_unknown = [
    u'No region',
]
region_order = _regions_north + _regions_south + _regions_unknown

_north_island = 'North Island'
_south_island = 'South Island'
_unknown_island = 'Unknown island'
island_order = [_north_island, _south_island, _unknown_island]

def _lookup_island(region):
    if region in _regions_north:
        return _north_island
    elif region in _regions_south:
        return _south_island
    elif region in _regions_unknown:
        return _unknown_island
    else:
        raise ValueError('unknown region: {}'.format(region))


class Hut(object):

    def __str__(self):
        return self.name

    def tag_with_visit(self, v):
        if self.name != v.name:
            raise ValueError('HutVisit {} does not correspond to Hut {}'.format(v.name, self.name))
        self.visited = True
        self.dates.append(v.arrival)
        if not self.sleep:
            self.sleep = v.sleep

    @classmethod
    def from_json(cls, obj):
        h = cls()

        props = obj['properties']
        geom = obj['geometry']

        h.name = unicode(props['name'])
        h.place = unicode(props['place'] or 'No place')
        h.region = unicode(props['region'] or 'No region')
        h.island = unicode(_lookup_island(h.region))
        h.status = props['status']
        h.lng = geom['coordinates'][0]
        h.lat = geom['coordinates'][1]

        # will be filled in later from HutVisit data
        h.visited = False
        h.dates = []
        h.sleep = False

        return h

def all_huts():
    huts_json = None
    with open(HUTS_FILE) as f:
        huts_json = json.load(f)
    huts_json_list = huts_json['features']

    huts_list = []
    for h in huts_json_list:
        huts_list.append(Hut.from_json(h))

    return huts_list

_places = list(set(map(lambda h: h.place, all_huts())))
place_order = sorted(_places)

_regions = list(set(map(lambda h: h.region, all_huts())))
assert len(_regions) == len(region_order)


if __name__ == '__main__':
    h = all_huts()
    print h[0]
    print len(place_order) # 116
    print len(region_order) # 20
