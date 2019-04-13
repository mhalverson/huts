'''
Utility for creating checklists of which huts have/haven't been visited.
'''

from hut import STATUS_OPEN, region_order, places_order
from merged import huts_enriched_with_visits, by_all, by_region, by_place


def checklist(huts_by_category, include_closed=True, sort_fn=None):
    '''Operates on a dictionary where the keys are categories and
    the values are lists of (enriched) Huts. Return a string that can
    be printed/written to file/etc. CLOSED huts will be included in
    the checklist unless include_closed is False. Sort order within
    each category defaults to the hut name, but can be customized by
    passing in a sort_fn. Sort order of the categories is fixed:
    regions will be printed in region_order (north to south), places
    in order of place name.

    Each checklist item will be preceded by a [ ] if visited, [X] if
    not visited and OPEN, or [-] if not visited and CLOSED.
    Huts will be listed by name.
    Huts that have been visited will be followed by a list of dates
    they were visited.
    Huts that have not been visited but not slept in will then be
    followed by '(have not slept in hut)'.
    ''' 
    result = []

    # determine category order
    categories = huts_by_category.keys()
    if len(categories) == 1:
        category_order = categories
    elif categories[0] in region_order:
        category_order = region_order
    else:
        category_order = places_order

    # determine hut ordering function
    if not sort_fn:
        sort_fn = lambda h: h.name

    total = 0
    visited = 0

    # for each category (in order)
    for c in category_order:
        huts = sorted(huts_by_category[c], key=sort_fn)
        if not include_closed:
            huts = filter(lambda h: h.status == STATUS_OPEN, huts)

        total_in_category = 0
        visited_in_category = 0
        for h in huts:
            total_in_category += 1
            total += 1
            if h.visited:
                visited_in_category += 1
                visited += 1
        result.append(u'{} ({} of {}):'.format(
            c.upper(), visited_in_category, total_in_category))

        for h in huts:
            checkbox_string = ''
            if h.visited:
                checkbox_string = '[X]'
            elif h.status != STATUS_OPEN:
                checkbox_string = '[-]'
            else:
                checkbox_string = '[ ]'
            visit_string = ''
            if h.dates:
                visit_string = ' (' + ' '.join(map(str, h.dates)) + ')'
            if h.visited and not h.sleep:
                visit_string += ' (did not sleep in hut)'
            result.append(u'{} {}{}'.format(checkbox_string, h.name, visit_string))

    result.append('TOTAL {} of {} visited'.format(visited, total))
    return result
        

if __name__ == '__main__':
    #for item in checklist(by_all(huts_enriched_with_visits())):
    #for item in checklist(by_place(huts_enriched_with_visits())):
    for item in checklist(by_region(huts_enriched_with_visits())):
            print item.encode('utf-8')
