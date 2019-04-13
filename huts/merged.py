'''
The all-important function: huts_enriched_with_visits(). Merges the data
from all_huts() with the data from all_hut_visits().

Also exposes functions for hierarchically sorting the huts:
by all (degenerate), by region, by place, or by region by place.
'''

from collections import defaultdict

from hut import all_huts
from trips import all_hut_visits


def huts_enriched_with_visits():
    '''Returns a list of all huts (open or closed) tagged with
    the HutVisit data from trips.'''
    huts = all_huts()
    for v in all_hut_visits():
        matches = filter(lambda h: h.name == v.name, huts)
        if len(matches) == 0:
            raise ValueError("hut doesn't exist: {}".format(v.name))
        elif len(matches) > 1:
            raise ValueError("multiple huts found with name: {}".format(v.name))
        [match]  = matches
        match.tag_with_visit(v)
    return huts

def by_all(huts):
    return {u'All huts': huts}  

def by_place(huts):
    result = defaultdict(list)
    for h in huts:
        result[h.place].append(h)
    return result

def by_region(huts):
    result = defaultdict(list)
    for h in huts:
        result[h.region].append(h)
    return result

def by_region_by_place(huts):
    result = defaultdict(lambda: defaultdict(list))
    for h in huts:
        result[h.region][h.place].append(h)
    return result

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
    from pprint import pprint
    h = all_huts()
    stats = summary(h)
    # pprint(sorted(stats['place'].items(), key=lambda x: x[1], reverse=True))
    # pprint(stats)

    # pprint(huts_by_place().keys())
    # pprint(huts_by_region().keys())
    for k, v in by_region_by_place(h).iteritems():
        for k2, v2 in v.iteritems():
            print k, k2, len(v2)

