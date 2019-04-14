'''
The all-important function: huts_enriched_with_visits(). Merges the data
from all_huts() with the data from all_hut_visits().

Also exposes a function for filtering huts:
    filter_open

Also exposes functions for hierarchically organizing the huts:
    by all (degenerate),
    by_island, by region, by place, 
    by_island_by_region, by_region_by_place,
    by_island_by_region_by_place.
'''

from collections import defaultdict

from hut import all_huts, island_order, region_order, place_order, STATUS_OPEN
from trips import all_hut_visits


def huts_enriched_with_visits():
    '''Returns a list of all huts (open or closed) tagged with
    the HutVisit data from trips.'''
    huts = all_huts()
    for v in all_hut_visits():
        matches = filter(lambda h: h.name == v.name, huts)
        if v.region:
            # honor the "region" disambiguator, if present
            matches = filter(lambda h: h.region == v.region, matches)
        if len(matches) == 0:
            raise ValueError("hut doesn't exist: {}".format(v.name))
        elif len(matches) > 1:
            raise ValueError("multiple huts found: {}".format(matches))
        [match]  = matches
        match.tag_with_visit(v)
    return huts

def by_all(huts):
    return {u'All huts': huts}  

def by_island(huts):
    result = defaultdict(list)
    for h in huts:
        result[h.island].append(h)
    return result

def by_region(huts):
    result = defaultdict(list)
    for h in huts:
        result[h.region].append(h)
    return result

def by_place(huts):
    result = defaultdict(list)
    for h in huts:
        result[h.place].append(h)
    return result

def by_island_by_region(huts):
    result = defaultdict(lambda: defaultdict(list))
    for h in huts:
        result[h.island][h.region].append(h)
    return result

def by_region_by_place(huts):
    result = defaultdict(lambda: defaultdict(list))
    for h in huts:
        result[h.region][h.place].append(h)
    return result

def by_island_by_region_by_place(huts):
    result = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for h in huts:
        result[h.island][h.region][h.place].append(h)
    return result

def filter_open(huts):
    return filter(lambda x: x.status == STATUS_OPEN, huts)

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
    dict_ = by_island_by_region_by_place(h)
    for i in island_order:
        huts_by_island = dict_[i]
        for r in region_order:
            if r in huts_by_island:
                huts_by_region = huts_by_island[r]
                for p in place_order:
                    if p in huts_by_region:
                        huts_by_place = huts_by_region[p]
                        # for hut in sorted(huts_by_place.keys()):
                        print i, r, p.encode('utf-8'), len(huts_by_place)
