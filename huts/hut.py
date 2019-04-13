'''
Defines the object representation of a Hut.
Exposes a list of all huts in New Zealand with all_huts().
Exposes lists of all places, all regions, and definitive sort-orders for both.
'''

from collections import defaultdict
import json
import os.path

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
HUTS_FILE = os.path.join(BASE_DIR, 'data', 'DOC_Huts.geojson')

STATUS_OPEN = 'OPEN'

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

places = list(set(map(lambda h: h.place, all_huts())))
places_order = sorted(places)
regions = list(set(map(lambda h: h.region, all_huts())))
region_order = [
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

    u'Nelson/Tasman',
    u'Marlborough',
    u'West Coast',
    u'Canterbury',
    u'Otago',
    u'Fiordland',
    u'Southland',

    u'No region',
    ]
assert len(regions) == len(region_order)


if __name__ == '__main__':
    h = all_huts()
    print h[0]
    print len(places) # 116
    print len(regions) # 20
