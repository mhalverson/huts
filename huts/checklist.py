'''
Utility for creating checklists of which huts have/haven't been visited.
'''
from collections import defaultdict

from hut import STATUS_OPEN, island_order, region_order, place_order
from merged import huts_enriched_with_visits


def checklist(huts_by_category, include_closed=True, sort_fn=None):
    '''Operates on a dictionary where the keys are categories and
    the values are lists of (enriched) Huts. Return a string that can
    be printed/written to file/etc. CLOSED huts will be included in
    the checklist unless include_closed is False. Sort order within
    each category defaults to the hut name, but can be customized by
    passing in a sort_fn. Sort order of the categories is fixed:
    islands will be printed in island_order (north to south), regions
    in region_order (north to south), places in place_order (alphabetical).

    Each hut in the checklist will be preceded by a [ ] if visited, [X] if
      not visited and OPEN, or [-] if not visited and CLOSED.
    Huts will be listed by name.
    Huts that have been visited will be followed by a list of dates
      they were visited.
    Huts that have been visited but not slept in will then be
      followed by '(have not slept in hut)'.
    ''' 
    if not include_closed:
        raise NotImplementedError('no ability to exclude closed yet')

    return checklist_recursive(huts_by_category, '', sort_fn=sort_fn)


def count_visits_recursive(huts_by_category):
    '''Given a dict, keys are categories, values are possibly nested categories.
    Returns another dict with the same keys, where the values are tuples of
    (huts visited, total huts) for each category.'''
    vals = huts_by_category.values()
    should_recur = (type(vals[0]) == type(defaultdict(list)))

    result = {}
    if not should_recur:
        for k, v in huts_by_category.iteritems():
            result[k] = (len(filter(lambda h: h.visited, v)), len(v))
    else:
        for k, v in huts_by_category.iteritems():
            recur_dict = count_visits_recursive(v)
            visited = 0
            total = 0
            for (subcategory_visited, subcategory_total) in recur_dict.values():
                visited += subcategory_visited
                total += subcategory_total
            result[k] = (visited, total)

    return result


INDENT_INCREMENT = 4 * ' '

def checklist_recursive(huts_by_category, indent, sort_fn=None):
    result = []

    # determine category order
    categories = huts_by_category.keys()
    if len(categories) == 1: # special for "by_all"
        category_order = categories
    elif categories[0] in island_order:
        category_order = island_order
    elif categories[0] in region_order:
        category_order = region_order
    elif categories[0] in place_order:
        category_order = place_order
    else:
        raise ValueError('unknown category: {}'.format(categories[0]))

    # determine if need to recur
    vals = huts_by_category.values()
    should_recur = (type(vals[0]) == type(defaultdict(list)))

    # prep the category counts
    category_counts = count_visits_recursive(huts_by_category)

    # the category_order is a total order; but we are only visiting a subset
    categories_to_visit = filter(lambda x: x in categories, category_order)
    for c in categories_to_visit:
        # print the category header
        visited_in_category = category_counts[c][0]
        total_in_category = category_counts[c][1]
        result.append(u'{}{} ({} of {}):'.format(indent, c.upper(), visited_in_category, total_in_category))

        # base case: we're at hut level so we just print the huts
        if not should_recur:
            if not sort_fn:
                sort_fn = lambda h: h.name

            huts = sorted(huts_by_category[c], key=sort_fn)
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
                result.append(u'{}{} {}{}'.format(indent + INDENT_INCREMENT, checkbox_string, h.name, visit_string))

        # recursive step: recur on the subcategories, increasing the indent
        else:
            sublist = checklist_recursive(huts_by_category[c], indent + INDENT_INCREMENT, sort_fn=sort_fn)
            result.extend(sublist)

    # shitty hack, print a grand total for the top-level
    if not indent:
        visited = sum([v[0] for v in category_counts.values()])
        total = sum([v[1] for v in category_counts.values()])
        result.append('GRAND TOTAL {} of {} visited'.format(visited, total))

    return result


if __name__ == '__main__':
    from merged import by_all, by_island, by_region, by_place, by_island_by_region, by_region_by_place, by_island_by_region_by_place
    #for item in checklist(by_all(huts_enriched_with_visits())):
    #for item in checklist(by_island(huts_enriched_with_visits())):
    #for item in checklist(by_region(huts_enriched_with_visits())):
    #for item in checklist(by_place(huts_enriched_with_visits())):
    #for item in checklist(by_island_by_region(huts_enriched_with_visits())):
    #for item in checklist(by_region_by_place(huts_enriched_with_visits())):
    for item in checklist(by_island_by_region_by_place(huts_enriched_with_visits())):
        print item.encode('utf-8')

    # for k, v in count_visits_recursive(by_island_by_region_by_place(huts_enriched_with_visits())).iteritems():
    #     print v[0], v[1], k.encode('utf-8')
    # print count_visits_recursive(by_region_by_place(huts_enriched_with_visits()))
    # print count_visits_recursive(by_island_by_region_by_place(huts_enriched_with_visits()))
