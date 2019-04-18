'''
Defines the object representation of a Hut.
Exposes a list of all DOC huts (and a few non-DOC huts) in New Zealand with all_huts().
Exposes lists of places, regions, and islands, as well as definitive sort-orders
for each.
'''

from collections import defaultdict
from datetime import timedelta
import json
import os.path

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DOC_HUTS_FILE = os.path.join(BASE_DIR, 'data', 'DOC_Huts.geojson')
NON_DOC_HUTS_FILE = os.path.join(BASE_DIR, 'data', 'non_DOC_Huts.json')

STATUS_OPEN = 'OPEN'


# TODO consider removing huts with unknown place or region
unknown_place = u'Unknown place'

regions_north = [
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
regions_south = [
    u'Nelson/Tasman',
    u'Marlborough',
    u'West Coast',
    u'Canterbury',
    u'Otago',
    u'Fiordland',
    u'Southland',
]
unknown_region = u'No region'
region_order = regions_north + regions_south + [unknown_region]

north_island = 'North Island'
south_island = 'South Island'
island_order = [north_island, south_island]

# Huts with unknown region / island will be assigned an island based on whether
# they're north or south of this latitude. NB this correctly classifies the
# island as of 2019-04-20, but if the Unknown Region huts change over time, it
# could incorrectly classify in the future.
UNKNOWN_REGION_DIVIDING_LATITUDE = -41.3881
def _lookup_island(region, lat):
    if region in regions_north:
        return north_island
    elif region in regions_south:
        return south_island

    if lat > UNKNOWN_REGION_DIVIDING_LATITUDE:
        return north_island
    else:
        return south_island


class Hut(object):

    def __str__(self):
        return self.name

    def tag_with_visit(self, v):
        '''mutate the object, adding data from the supplied HutVisit'''
        if self.name != v.name:
            raise ValueError('HutVisit {} does not correspond to Hut {}'.format(v.name, self.name))
        self.visited = True
        self.dates.append((v.arrival, v.num_days))
        if not self.sleep:
            self.sleep = v.sleep

    def render_name_with_link(self):
        if self.url:
            return u'<a href="{}">{}</a>'.format(self.url, self.name)

        return self.name

    def render_dates_visited(self):
        'Collapses date ranges'
        strs = []
        for date, num_days in self.dates:
            if num_days == 1:
                strs.append(str(date))
            else:
                start = str(date)
                end = str(date + timedelta(days=num_days - 1))
                strs.append('{} to {}'.format(start,end))
        return ', '.join(strs)

    @classmethod
    def from_geojson(cls, obj, doc_maintained=True):
        h = cls()

        props = obj['properties']
        geom = obj['geometry']

        h.name = unicode(props['name']).strip()
        h.place = unicode(props['place'] or unknown_place)
        h.region = unicode(props['region'] or unknown_region)
        h.lng = geom['coordinates'][0]
        h.lat = geom['coordinates'][1]
        h.island = unicode(_lookup_island(h.region, h.lat))
        h.status = props['status']
        h.url = props['staticLink']

        h.doc_maintained = doc_maintained

        # will be filled in later from HutVisit data
        h.visited = False
        h.dates = []
        h.sleep = False

        return h

    @classmethod
    def from_json(cls, obj, doc_maintained=False):
        '''special hand-crafted dataset of non-DOC maintained huts
        that I have visited'''
        h = cls()

        h.name = unicode(obj['name'])
        h.place = unicode(obj['place'])
        h.region = unicode(obj['region'])
        h.island = unicode(obj['island'])
        h.lng = obj['lng']
        h.lat = obj['lat']
        h.url = obj['staticLink']

        h.doc_maintained = doc_maintained

        # will be filled in later from HutVisit data
        h.visited = False
        h.dates = []
        h.sleep = False

        return h

def _doc_huts():
    huts_json = None
    with open(DOC_HUTS_FILE) as f:
        huts_json = json.load(f)
    huts_json_list = huts_json['features']

    huts_list = []
    for h in huts_json_list:
        huts_list.append(Hut.from_geojson(h))

    return huts_list

def _non_doc_huts():
    huts_json = None
    with open(NON_DOC_HUTS_FILE) as f:
        huts_json = json.load(f)

    huts_list = []
    for h in huts_json:
        huts_list.append(Hut.from_json(h))

    return huts_list

def all_huts():
    return _doc_huts() + _non_doc_huts()

_places = list(set(map(lambda h: h.place, all_huts())))
place_order = sorted(_places)

_regions = list(set(map(lambda h: h.region, all_huts())))
assert len(_regions) == len(region_order)


if __name__ == '__main__':
    h = all_huts()
    print h[0]
    print len(place_order) # 116
    print len(region_order) # 20
