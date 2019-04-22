'''
Utility for creating checklists of which huts have/haven't been visited.
'''
from collections import defaultdict

from huts.hut import STATUS_OPEN, island_order, region_order, place_order


def newline(html):
    if html:
        return '<br/>'
    return '\n'


def header(html):
    return newline(html).join([
        'Hut names are links to the DOC page for the hut (except for the few huts not in the official DOC list).',
        'Some of the huts also have links to photos/blog posts/reports for the trip where I visited the hut. These are typically Facebook posts and may not be publicly accessible.',
    ])


def _intersperse(iterable, delimiter):
    it = iter(iterable)
    yield next(it)
    for x in it:
        yield delimiter
        yield x


def checklist(huts_by_category, sort_fn=None, html=False):
    '''Operates on a dictionary where the keys are categories and
    the values are lists of (enriched) Huts. Return a string that can
    be printed/written to file/etc. Sort order within each category
    defaults to the hut name, but can be customized by passing in a
    sort_fn. Sort order of the categories is fixed:
      - islands will be printed in island_order (north to south),
      - regions in region_order (north to south),
      - places in place_order (alphabetical).

    For plaintext rendering (when html=False):
    Each hut in the checklist will be preceded by a [ ] if visited, [X] if
      not visited and OPEN, or [-] if not visited and CLOSED.
    Huts will be listed by name.
    Huts that have been visited will be followed by a list of dates
      they were visited.
    Huts that have been visited but not slept in will then be
      followed by '(have not slept in hut)'.

    For html rendering (when html=True):
    Hut name will be an anchor pointing to the hut's url.
    Links to trip reports will be added to the date strings.
    ''' 
    result = checklist_recursive(huts_by_category, '', sort_fn, html)
    if html:
        return list(_intersperse(result, newline(html)))
    else:
        return result


def count_visits_recursive(huts_by_category):
    '''Given a dict, keys are categories, values are possibly nested categories.
    Returns another dict with the same keys, where the values are tuples of
    (huts visited, total huts) for each category.'''
    vals = list(huts_by_category.values())
    should_recur = (type(vals[0]) == type(defaultdict(list)))

    result = {}
    if not should_recur:
        for k, v in huts_by_category.items():
            result[k] = (len(list(filter(lambda h: h.visited, v))), len(v))
    else:
        for k, v in huts_by_category.items():
            recur_dict = count_visits_recursive(v)
            visited = 0
            total = 0
            for (subcategory_visited, subcategory_total) in recur_dict.values():
                visited += subcategory_visited
                total += subcategory_total
            result[k] = (visited, total)

    return result


def checklist_recursive(huts_by_category, indent, sort_fn, html):
    if html:
        indent_char = '&nbsp;'
    else:
        indent_char = ' '
    INDENT_INCREMENT = 8 * indent_char

    result = []

    # determine category order
    categories = set(huts_by_category.keys())
    if len(categories) == 1: # special for "by_all"
        category_order = categories
    elif categories.intersection(set(island_order)):
        category_order = island_order
    elif categories.intersection(set(region_order)):
        category_order = region_order
    elif categories.intersection(set(place_order)):
        category_order = place_order
    else:
        raise ValueError('unknown category: {}'.format(categories[0]))

    # determine if need to recur
    vals = list(huts_by_category.values())
    should_recur = (type(vals[0]) == type(defaultdict(list)))

    # prep the category counts
    category_counts = count_visits_recursive(huts_by_category)

    # the category_order is a total order; but we are only visiting a subset
    categories_to_visit = filter(lambda x: x in categories, category_order)
    for c in categories_to_visit:
        # print the category header
        visited_in_category = category_counts[c][0]
        total_in_category = category_counts[c][1]
        if total_in_category == 0:
            # can occur if we're excluding closed huts
            continue
        result.append(u'{}{} ({} of {}):'.format(indent, c.upper(), visited_in_category, total_in_category))

        # base case: we're at hut level so we just print the huts
        if not should_recur:
            if not sort_fn:
                sort_fn = lambda h: h.name

            huts = sorted(huts_by_category[c], key=sort_fn)
            for h in huts:
                checkbox_string = ''
                if h.visited:
                    checkbox_string = '\u2611'  if html else '[X]'
                elif h.status != STATUS_OPEN:
                    checkbox_string = '\u2610' if html else '[-]'
                else:
                    checkbox_string = '\u2610' if html else '[ ]'
                name_string = h.render_name(html=html)
                if not h.doc_maintained:
                    name_string += ' (not DOC maintained)'
                visit_string = ''
                if h.visited:
                    visit_string = ' ({})'.format(h.render_dates_visited(html=html))
                if h.visited and not h.sleep:
                    visit_string += ' (did not sleep in hut)'
                result.append(u'{}{} {}{}'.format(indent + INDENT_INCREMENT, checkbox_string, name_string, visit_string))

        # recursive step: recur on the subcategories, increasing the indent
        else:
            sublist = checklist_recursive(huts_by_category[c], indent + INDENT_INCREMENT, sort_fn, html)
            result.extend(sublist)

    # shitty hack, print a grand total for the top-level
    if not indent:
        visited = sum([v[0] for v in category_counts.values()])
        total = sum([v[1] for v in category_counts.values()])
        result.append('TOTAL {} of {} visited'.format(visited, total))

    return result

if __name__ == '__main__':
    import sys
    from huts.merged import (
            huts_enriched_with_trips,
            by_all, by_island, by_region, by_place,
            by_island_by_region, by_region_by_place,
            by_island_by_region_by_place,
            filter_open, filter_known_region_known_place,
    )
    huts = filter_known_region_known_place(huts_enriched_with_trips())

    html = len(sys.argv) > 1 and sys.argv[1] == 'html'
    if html:
        print(header(html))
        print(2 * newline(html))
    for item in checklist(by_island_by_region_by_place(huts), html=html):
        print(item)
