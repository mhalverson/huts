'''
Contains the object representation of a Trip and HutVisit.
Contains the raw-data record of all trips taken.
Exposes all trips taken with all_trips() and all hut visits with all_hut_visits().
'''

from datetime import date

TRIP_START = 'trip_start' # date
TRIP_END = 'trip_end' # date
TRIP_DESC = 'trip_desc' # string, brief name / description of the trip
TRIP_PARTY = 'party' # list of strings of (other) party members' names
TRIP_ABORTED = 'aborted' # bool, did we have to abort the trip, defaults to false
TRIP_REPORT = 'report' # URL for blogpost, photos, trip report, etc
TRIP_HUTS = 'huts' # list of dicts with the following keys:
HUT_NAME = 'hut_name' # string
HUT_REGION = 'hut_region' # string, used to disambiguate huts with the same name
HUT_ARRIVAL = 'hut_arrival' # date
HUT_SLEEP = 'hut_sleep' # bool, did I sleep in the hut or just pass through


template = '''
    {
        TRIP_START: date(2019, ),
        TRIP_END: date(2019, ),
        TRIP_DESC: '',
        TRIP_PARTY: [],
        TRIP_ABORTED: False,
        TRIP_REPORT: None,
        TRIP_HUTS: [{HUT_ARRIVAL: date(2019, ), HUT_SLEEP: , HUT_NAME: u'', HUT_REGION: ''},
                    {HUT_ARRIVAL: date(2019, ), HUT_SLEEP: , HUT_NAME: u'', HUT_REGION: ''},]
    },
'''

trips_raw = [
    # trips_raw gets translated into a list of Trips and a list of HutVisits
    {
        TRIP_START: date(2010, 3, 6),
        TRIP_END: date(2010, 3, 7),
        TRIP_DESC: 'CUTC Freshers at Mt Somers',
        TRIP_PARTY: ['Katrina McCall', 'Martina Kratt', 'Sharon Hornblow', 'Becky Le Lievre'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2010, 3, 6), HUT_SLEEP: False, HUT_NAME: u'Woolshed Creek Hut'},],
    },
]

class Trip(object):
    @classmethod
    def from_dict(cls, dict_):
        t = cls()
        t.start = dict_[TRIP_START]
        t.end = dict_[TRIP_END]
        t.desc = dict_[TRIP_DESC]
        t.party = dict_.get(TRIP_PARTY, "don't remember")
        t.aborted = dict_.get(TRIP_PARTY, False)
        t.report = dict_.get(TRIP_REPORT)
        t.huts = [HutVisit.from_dict(hv) for hv in dict_.get(TRIP_HUTS, [])]
        return t

    def __str__(self):
        return 'Trip: {}'.format(self.desc)


class HutVisit(object):
    @classmethod
    def from_dict(cls, dict_):
        hv = cls()
        hv.name = dict_[HUT_NAME]
        hv.region = dict_.get(HUT_REGION)
        hv.arrival = dict_[HUT_ARRIVAL]
        hv.sleep = dict_[HUT_SLEEP]
        return hv

    def __str__(self):
        return 'HutVisit: {}'.format(self.name)

def all_trips():
    return [Trip.from_dict(t) for t in trips_raw]

def all_hut_visits():
    result = []
    for t in all_trips():
        result.extend(t.huts)
    return result


if __name__ == '__main__':
    trips = all_trips()
    from pprint import pprint
    pprint([str(t) for t in trips])

    hv = all_hut_visits()
    pprint([str(x) for x in hv])
