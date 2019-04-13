'''
Defines the object representation of a Hut.
Exposes a list of all huts in New Zealand with all_huts().
'''

from collections import defaultdict
import json
import os.path

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
HUTS_FILE = os.path.join(BASE_DIR, 'data', 'DOC_Huts.geojson')

class Hut(object):

    def __str__(self):
        return self.name

    @classmethod
    def from_json(cls, obj):
        h = cls()

        props = obj['properties']
        geom = obj['geometry']

        h.name = props['name']
        h.place = props['place']
        h.region = props['region']
        h.status = props['status']
        h.lng = geom['coordinates'][0]
        h.lat = geom['coordinates'][1]

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


def summary(huts):
    total = 0
    place = defaultdict(int)
    region = defaultdict(int)
    status = defaultdict(int)
    for h in huts:
        total += 1
        place[h.place] += 1
        region[h.region] += 1
        status[h.status] += 1
    return {'total': total,
            'place': place,
            'region': region,
            'status': status}


if __name__ == '__main__':
    h = all_huts()
    print h[0]
    stats = summary(h)
    from pprint import pprint
    pprint(sorted(stats['place'].items(), key=lambda x: x[1], reverse=True))
