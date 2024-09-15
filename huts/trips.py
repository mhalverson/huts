'''
Contains the object representation of a Trip and HutVisit.
Contains the raw-data record of all trips taken.
Exposes all trips taken with all_trips() and all hut visits with all_hut_visits().
'''

from datetime import date

TRIP_START = 'trip_start' # date, required
TRIP_END = 'trip_end' # date, required
TRIP_DESC = 'trip_desc' # string, brief name / description of the trip, required
TRIP_PARTY = 'party' # list of strings of (other) party members' names, defaults to ["don't remember"]
TRIP_ABORTED = 'aborted' # bool, did we have to abort the trip, defaults to false
TRIP_REPORTS = 'reports' # list of strings of URLs for blogpost, photos, trip report; defaults to []
TRIP_HUTS = 'huts' # list of dicts with the following keys; defaults to []
HUT_NAME = 'hut_name' # string, required
HUT_REGION = 'hut_region' # string, used to disambiguate huts with the same name, defaults to None
HUT_ARRIVAL = 'hut_arrival' # date, required
HUT_SLEEP = 'hut_sleep' # bool, did I sleep in the hut or just pass through, required
HUT_MULTIPLE_NIGHTS = 'hut_multiple_nights' # if multiple nights spent in the same hut, how many nights total; defaults to 1
HUT_IS_DOC_MAINTAINED = 'hut_is_doc_maintained' # bool, if it's not maintained by DOC then won't try to look it up; defaults to True


template = '''
    {
        TRIP_START: date(2021, ),
        TRIP_END: date(2021, ),
        TRIP_DESC: '',
        TRIP_ABORTED: True,
        TRIP_REPORTS: [''],
        TRIP_PARTY: [],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2019, ), HUT_SLEEP: , HUT_NAME: u'', HUT_REGION: '', HUT_IS_DOC_MAINTAINED: False, HUT_MULTIPLE_NIGHTS: 2},
                    {HUT_ARRIVAL: date(2019, ), HUT_SLEEP: , HUT_NAME: u''},]
    },
'''

trips_raw = [
    # trips_raw gets translated into a list of Trips and a list of HutVisits
    {
        TRIP_START: date(2010, 3, 6),
        TRIP_END: date(2010, 3, 7),
        TRIP_DESC: 'CUTC Freshers at Mt Somers',
        TRIP_REPORTS: ['https://www.facebook.com/sophie.kerr.585/posts/1290990667460'],
        TRIP_PARTY: ['Katrina McCall', 'Martina Kratt', 'Sharon Hornblow', 'Becky Le Lievre', 'Ben Richards', '50 other people'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2010, 3, 6), HUT_SLEEP: False, HUT_NAME: u'Woolshed Creek Hut'},],
    },
    {
        TRIP_START: date(2010, 4, 2),
        TRIP_END: date(2010, 2, 5),
        TRIP_DESC: 'Frew Saddle Circuit',
        TRIP_REPORTS: ['https://www.facebook.com/volker.nock/media_set?set=a.388888786471&type=3'], # Volker's photo album
        TRIP_PARTY: ['Volker Nock', 'Martin Lennernas', 'Julia MV', 'Katrina Kenah'],
        TRIP_HUTS: [
            {HUT_ARRIVAL: date(2010, 4, 2), HUT_SLEEP: True, HUT_NAME: u'Cedar Flat Hut'},
            {HUT_ARRIVAL: date(2010, 4, 2), HUT_SLEEP: False, HUT_NAME: u'Historic Cedar Flat Hut'},
            {HUT_ARRIVAL: date(2010, 4, 3), HUT_SLEEP: False, HUT_NAME: u'Top Toaroha Hut'},
            {HUT_ARRIVAL: date(2010, 4, 3), HUT_SLEEP: False, HUT_NAME: u'Toaroha Saddle Bivvy'},
            {HUT_ARRIVAL: date(2010, 4, 3), HUT_SLEEP: True, HUT_NAME: u'Poet Hut'},
            {HUT_ARRIVAL: date(2010, 4, 4), HUT_SLEEP: False, HUT_NAME: u'Bluff Hut'},
            {HUT_ARRIVAL: date(2010, 4, 4), HUT_SLEEP: False, HUT_NAME: u'Frew Saddle Bivvy'},
            {HUT_ARRIVAL: date(2010, 4, 4), HUT_SLEEP: True, HUT_NAME: u'Frew Hut'},
            {HUT_ARRIVAL: date(2010, 4, 5), HUT_SLEEP: False, HUT_NAME: u'Rapid Creek Hut'},
            ],
    },
    {
        TRIP_START: date(2010, 5, 2),
        TRIP_END: date(2010, 5, 2),
        TRIP_DESC: 'Mt Tinline',
        TRIP_REPORTS: ['https://www.facebook.com/mhhalverson/media_set?set=a.1451615844129&type=3'],
    },
    {
        TRIP_START: date(2010, 5, 9),
        TRIP_END: date(2010, 5, 9),
        TRIP_DESC: "Bob's Bivvy",
        TRIP_REPORTS: ['https://www.facebook.com/mhhalverson/media_set?set=a.1451627084410&type=3'],
        TRIP_PARTY: ['Laurie Slesar', 'Martina Kratt', 'others'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2010, 5, 9), HUT_SLEEP: False, HUT_NAME: u"Bob's Camp Bivvy"},],
    },
    {
        TRIP_START: date(2010, 5, 22),
        TRIP_END: date(2010, 5, 23),
        TRIP_DESC: 'Ice climbing at Franz Josef',
        TRIP_REPORTS: ['https://www.facebook.com/mhhalverson/media_set?set=a.1451726206888&type=3'],
        TRIP_PARTY: ['Becky Le Lievre', 'Martina Kratt', 'Katrina McCall', 'Oli Marsh', 'Dave Manning', 'Kirstie McHale', 'Jana Ringleb', 'others'],
    },
    {
        TRIP_START: date(2010, 5, 29),
        TRIP_END: date(2010, 5, 30),
        TRIP_DESC: 'TWALK 2010',
        TRIP_REPORTS: ['https://www.facebook.com/mhhalverson/media_set?set=a.1451768327941&type=3'],
        TRIP_PARTY: ['Laurie Slesar', 'Katrina McCall', 'Becky Le Lievre', 'Wesley', 'Martina Kratt'],
    },
    {
        TRIP_START: date(2010, 6, 5),
        TRIP_END: date(2010, 6, 8),
        TRIP_DESC: 'Routeburn/Caples',
        TRIP_REPORTS: ['https://www.facebook.com/mhhalverson/media_set?set=a.1451784848354&type=3'],
        TRIP_PARTY: ['Dave Manning', 'Sophie Manning', 'Jana Ringleb'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2010, 6, 5), HUT_SLEEP: True, HUT_NAME: u'Routeburn Flats Hut'},
                    {HUT_ARRIVAL: date(2010, 6, 6), HUT_SLEEP: False, HUT_NAME: u'Routeburn Falls Hut'},
                    {HUT_ARRIVAL: date(2010, 6, 6), HUT_SLEEP: True, HUT_NAME: u'Lake Mackenzie Hut'},
                    {HUT_ARRIVAL: date(2010, 6, 7), HUT_SLEEP: False, HUT_NAME: u'Lake Howden Hut'},
                    {HUT_ARRIVAL: date(2010, 6, 7), HUT_SLEEP: True, HUT_NAME: u'Upper Caples Hut', HUT_IS_DOC_MAINTAINED: False},
                    {HUT_ARRIVAL: date(2010, 6, 8), HUT_SLEEP: False, HUT_NAME: u'Mid Caples Hut'},
                    ]
    },
    {
        TRIP_START: date(2010, 6, 29),
        TRIP_END: date(2010, 7, 2),
        TRIP_DESC: 'Lake Angelus',
        TRIP_REPORTS: ['https://www.facebook.com/mhhalverson/posts/142603295754528',
                       'https://www.facebook.com/mhhalverson/timeline/story?ut=60&wstart=1262332800&wend=1293868799&hash=6317922248107894672&pagefilter=3'],
        TRIP_PARTY: ['Brian Thorne', 'Neville Thorne', 'Kirstie McHale', 'Becky Le Lievre'],
        TRIP_HUTS: [ # not totally sure about these dates, but I think that's what we did. I know we came
                     # back along Robert Ridge.
                    {HUT_ARRIVAL: date(2010, 6, 29), HUT_SLEEP: False, HUT_NAME: u'Speargrass Hut'},
                    {HUT_ARRIVAL: date(2010, 6, 29), HUT_SLEEP: True, HUT_NAME: u'Sabine Hut'},
                    {HUT_ARRIVAL: date(2010, 6, 30), HUT_SLEEP: True, HUT_NAME: u'Angelus Hut', HUT_MULTIPLE_NIGHTS: 2},
                    ]
    },
    {
        TRIP_START: date(2010, 7, 2),
        TRIP_END: date(2010, 7, 7),
        TRIP_DESC: 'Nelson Lakes traverse',
        TRIP_REPORTS: ['https://www.facebook.com/mhhalverson/posts/141462382537390',
                       'https://blog.thorne.link/2010/08/midwinter-nelson-lakes-tramping.html',
                       'https://www.facebook.com/mhhalverson/timeline/story?ut=60&wstart=1262332800&wend=1293868799&hash=6317922248107894672&pagefilter=3'],
        TRIP_PARTY: ['Brian Thorne', 'Neville Thorne'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2010, 7, 2), HUT_SLEEP: True, HUT_NAME: u'Coldwater Hut'}, # may have been Lakehead Hut, hard to say
                    {HUT_ARRIVAL: date(2010, 7, 3), HUT_SLEEP: False, HUT_NAME: u'John Tait Hut'},
                    {HUT_ARRIVAL: date(2010, 7, 3), HUT_SLEEP: True, HUT_NAME: u'Upper Travers Hut'},
                    {HUT_ARRIVAL: date(2010, 7, 4), HUT_SLEEP: False, HUT_NAME: u'West Sabine Hut'},
                    {HUT_ARRIVAL: date(2010, 7, 4), HUT_SLEEP: True, HUT_NAME: u'Blue Lake Hut'},
                    {HUT_ARRIVAL: date(2010, 7, 6), HUT_SLEEP: False, HUT_NAME: u'East Matakitaki Hut'},
                    {HUT_ARRIVAL: date(2010, 7, 6), HUT_SLEEP: True, HUT_NAME: u'Bobs Hut'},
                    {HUT_ARRIVAL: date(2010, 7, 7), HUT_SLEEP: False, HUT_NAME: u'Ada Pass Hut'},
                    {HUT_ARRIVAL: date(2010, 7, 7), HUT_SLEEP: False, HUT_NAME: u'Cannibal Gorge Hut'},
                    ]
    },
    {
        TRIP_START: date(2010, 7, 17),
        TRIP_END: date(2010, 7, 18),
        TRIP_DESC: 'Refreshers at Otehake',
        TRIP_REPORTS: ['https://www.facebook.com/mhhalverson/posts/1493180403217'],
        TRIP_PARTY: ['Sophie Manning', 'Shannon Harley', 'Katrina McCall', 'Dave Manning', 'Hannah Johns', 'others'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2010, 7, 17), HUT_SLEEP: False, HUT_NAME: u'Otehake Hut'},],
    },
    {
        TRIP_START: date(2010, 7, 24),
        TRIP_END: date(2010, 7, 25),
        TRIP_DESC: 'Snowcraft - Temple Basin',
        TRIP_REPORTS: ['https://www.facebook.com/mhhalverson/timeline/story?ut=60&wstart=1262332800&wend=1293868799&hash=-7672385450074425389&pagefilter=3',
                       'https://www.facebook.com/mhhalverson/posts/1498500816224',
                       'https://www.facebook.com/photo.php?fbid=1351934048305&set=a.1351919487941&type=3&theater',
                       'https://www.facebook.com/photo.php?fbid=1351919847950&set=a.1351919487941&type=3&theater',
                       'https://www.facebook.com/mhhalverson/posts/105572962830857',
                       'https://www.facebook.com/photo.php?fbid=459899371256&set=a.459898906256&type=3&theater',
                      ],
        TRIP_PARTY: ['Brian Thorne', 'Sophie Manning', 'Dave Manning', 'Ellen Ashmore', 'Oli Marsh', 'Eng Eu', 'others'],
    },
    {
        TRIP_START: date(2010, 8, 7),
        TRIP_END: date(2010, 8, 8),
        TRIP_DESC: 'Bushball',
        TRIP_PARTY: ['many'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2010, 8, 7), HUT_SLEEP: True, HUT_NAME: u'Cannibal Gorge Hut'},],
    },
    {
        TRIP_START: date(2010, 8, 21),
        TRIP_END: date(2010, 8, 30),
        TRIP_DESC: 'Stewart Island Northwest Circuit',
        TRIP_REPORTS: ['https://www.facebook.com/mhhalverson/timeline/story?ut=60&wstart=1262332800&wend=1293868799&hash=763828292110300438&pagefilter=3',
                       'https://www.facebook.com/mhhalverson/timeline/story?ut=60&wstart=1262332800&wend=1293868799&hash=7002941862173070228&pagefilter=3'],
        TRIP_PARTY: ['David Gombrii', 'Oli Weller', 'Monique Eade', 'Becky Le Lievre', 'Martina Kratt', 'Shannon Harley'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2010, 8, 21), HUT_SLEEP: True, HUT_NAME: u'Port William Hut'},
                    {HUT_ARRIVAL: date(2010, 8, 22), HUT_SLEEP: True, HUT_NAME: u'Bungaree Hut'},
                    {HUT_ARRIVAL: date(2010, 8, 23), HUT_SLEEP: True, HUT_NAME: u'Christmas Village Hut'},
                    {HUT_ARRIVAL: date(2010, 8, 24), HUT_SLEEP: True, HUT_NAME: u'Yankee River Hut'},
                    {HUT_ARRIVAL: date(2010, 8, 25), HUT_SLEEP: False, HUT_NAME: u'Long Harry Hut'},
                    {HUT_ARRIVAL: date(2010, 8, 25), HUT_SLEEP: True, HUT_NAME: u'East Ruggedy Hut', HUT_MULTIPLE_NIGHTS: 2},
                    {HUT_ARRIVAL: date(2010, 8, 27), HUT_SLEEP: True, HUT_NAME: u'Big Hellfire Hut'},
                    {HUT_ARRIVAL: date(2010, 8, 28), HUT_SLEEP: True, HUT_NAME: u'Mason Bay Hut'},
                    {HUT_ARRIVAL: date(2010, 8, 29), HUT_SLEEP: True, HUT_NAME: u'Freshwater Hut'},
                    {HUT_ARRIVAL: date(2010, 8, 30), HUT_SLEEP: False, HUT_NAME: u'North Arm Hut'},
                    ]
    },
    # Hollyford UCCC trip (2010 Sep ?2? - ?4?) https://www.facebook.com/mhhalverson/media_set?set=a.1554515216549&type=3
    # (failed) Lake Man Biv (2010 Sep 13 - 14) none, Sophie and I just camped in the shelter at the Windy Point carpark :)
    {
        TRIP_START: date(2010, 10, 23),
        TRIP_END: date(2010, 10, 24),
        TRIP_DESC: 'Carroll Hut',
        TRIP_REPORTS: ['https://www.facebook.com/mhhalverson/timeline/story?ut=60&wstart=1262332800&wend=1293868799&hash=6925261572058883915&pagefilter=3',
                       'https://www.facebook.com/sophie.kerr.585/media_set?set=a.1528766091697&type=3'],
        TRIP_PARTY: ['Sophie Manning', 'Becky Le Lievre'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2010, 10, 23), HUT_SLEEP: True, HUT_NAME: u'Carroll Hut'}]
    },
    {
        TRIP_START: date(2010, 10, 30),
        TRIP_END: date(2010, 11, 2),
        TRIP_DESC: 'Smythe Hut',
        TRIP_REPORTS: [], # TROG 2010
        TRIP_PARTY: [], # solo!
        TRIP_HUTS: [{HUT_ARRIVAL: date(2010, 10, 30), HUT_SLEEP: True, HUT_NAME: u'Hunters Hut', HUT_REGION: 'West Coast'},
                    {HUT_ARRIVAL: date(2010, 10, 31), HUT_SLEEP: True, HUT_NAME: u'Smyth Hut'},
                    {HUT_ARRIVAL: date(2010, 11, 1), HUT_SLEEP: True, HUT_NAME: u'Hunters Hut', HUT_REGION: 'West Coast'},
                    ]
    },
    {
        TRIP_START: date(2010, 11, 15),
        TRIP_END: date(2010, 11, 16),
        TRIP_DESC: 'Rees/Dart Track',
        TRIP_ABORTED: True,  # bad weather - rivers were flooded, snow on the pass IIRC
        TRIP_REPORTS: ['https://www.facebook.com/mhhalverson/timeline/story?ut=60&wstart=1262332800&wend=1293868799&hash=6550845421681570440&pagefilter=3'],
        TRIP_PARTY: ['Becky Le Lievre', 'Monique Eade', 'Sharon Hornblow', 'Martina Kratt'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2010, 11, 15), HUT_SLEEP: True, HUT_NAME: u'Shelter Rock Hut'}]
    },
    {
        TRIP_START: date(2010, 11, 18),
        TRIP_END: date(2010, 11, 21),
        TRIP_DESC: 'Gillespie Pass Circuit',
        TRIP_REPORTS: ['https://www.facebook.com/photo.php?fbid=1670380993121&set=a.1670376833017&type=3&theater',
                       'https://www.facebook.com/mhhalverson/posts/1670403193676',
                       'https://www.facebook.com/mhhalverson/posts/1709475050448',],
        TRIP_PARTY: ['Monique Eade', 'Becky Le Lievre',],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2010, 11, 18), HUT_SLEEP: True, HUT_NAME: u'Young Hut'},
                    {HUT_ARRIVAL: date(2010, 11, 19), HUT_SLEEP: True, HUT_NAME: u'Siberia Hut', HUT_REGION: 'Otago', HUT_MULTIPLE_NIGHTS: 2},
                    ]
    },
    {
        TRIP_START: date(2010, 11, 23),
        TRIP_END: date(2010, 11, 30),
        TRIP_DESC: 'Dusky Track',
        TRIP_REPORTS: ['https://www.facebook.com/mhhalverson/posts/1670403193676',
                       'https://www.facebook.com/mhhalverson/posts/1709475050448',],
        TRIP_PARTY: ['Neville Thorne', 'Monique Eade', 'Becky Le Lievre'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2010, 11, 23), HUT_SLEEP: True, HUT_NAME: u'Upper Spey Hut'},
                    {HUT_ARRIVAL: date(2010, 11, 24), HUT_SLEEP: True, HUT_NAME: u'Kintail Hut'},
                    {HUT_ARRIVAL: date(2010, 11, 25), HUT_SLEEP: True, HUT_NAME: u'Loch Maree Hut'},
                    {HUT_ARRIVAL: date(2010, 11, 26), HUT_SLEEP: True, HUT_NAME: u'Lake Roe Hut'},
                    {HUT_ARRIVAL: date(2010, 11, 27), HUT_SLEEP: True, HUT_NAME: u'Loch Maree Hut'},
                    {HUT_ARRIVAL: date(2010, 11, 28), HUT_SLEEP: True, HUT_NAME: u'Kintail Hut'},
                    {HUT_ARRIVAL: date(2010, 11, 29), HUT_SLEEP: True, HUT_NAME: u'Upper Spey Hut'},
                    ]
    },
    {
        TRIP_START: date(2010, 12, 6),
        TRIP_END: date(2010, 12, 14),
        TRIP_DESC: 'Murchisons heli trip',
        TRIP_REPORTS: ['https://blog.thorne.link/2011/11/come-on-irene.html',
                       'https://www.facebook.com/mhhalverson/timeline/story?ut=60&wstart=1262332800&wend=1293868799&hash=-7539433584117429412&pagefilter=3',
                       'https://www.facebook.com/mhhalverson/timeline/story?ut=60&wstart=1262332800&wend=1293868799&hash=-9096106369157703868&pagefilter=3',
                       'https://www.facebook.com/mhhalverson/posts/1709475050448'],
        TRIP_PARTY: ['Brian Thorne', 'Giselle Clarkson'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2010, 12, 8), HUT_SLEEP: True, HUT_NAME: u'Robin Saddle Hut',
                     HUT_IS_DOC_MAINTAINED: False, HUT_MULTIPLE_NIGHTS: 3}] # guessing on the dates / number of nights here.
    },
    {
        TRIP_START: date(2010, 12, 18), # iffy on the date
        TRIP_END: date(2010, 12, 18),
        TRIP_DESC: 'Mt Cheeseman dayhike',
        TRIP_REPORTS: ['https://www.facebook.com/mhhalverson/posts/1709475050448'],
        TRIP_PARTY: ['Rune Thing', 'others'],
    },
    {
        TRIP_START: date(2010, 12, 20), # iffy on the date
        TRIP_END: date(2010, 12, 20),
        TRIP_DESC: 'Mt Herbert dayhike',
        TRIP_REPORTS: ['https://www.facebook.com/mhhalverson/timeline/story?ut=60&wstart=1262332800&wend=1293868799&hash=-9120185976699389213&pagefilter=3',
                       'https://www.facebook.com/mhhalverson/timeline/story?ut=60&wstart=1262332800&wend=1293868799&hash=-6185755761823045467&pagefilter=3',
                       'https://www.facebook.com/mhhalverson/posts/1709475050448'],
        TRIP_PARTY: ['Harriet Hughes', 'Sophia Ai', 'Kerry Bellringer'],
    },
    {
        TRIP_START: date(2013, 2, 24),
        TRIP_END: date(2013, 2, 24),
        TRIP_DESC: 'Avalanche Peak dayhike',
        TRIP_REPORTS: ['https://www.facebook.com/photo.php?fbid=10151534590010992&set=a.10151534589925992&type=3&theater',
                       'https://www.facebook.com/photo.php?fbid=10151534590135992&set=a.10151534589925992&type=3&theater'],
        TRIP_PARTY: ['Adam Kuang', 'Brian Thorne', 'Dave Manning', 'Sophie Manning', 'Giselle Clarkson'],
    },
    {
        TRIP_START: date(2013, 3, 1),
        TRIP_END: date(2013, 3, 8),
        TRIP_DESC: 'Ivory Lake Hut',
        TRIP_REPORTS: ['https://www.facebook.com/giselle.clarkson/posts/518434537927'],
        TRIP_PARTY: ['Brian Thorne', 'Giselle Clarkson'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2013, 3, 1), HUT_SLEEP: True, HUT_NAME: u'Kiwi Flat Hut'}, # fuzzy on the dates here.
                    {HUT_ARRIVAL: date(2013, 3, 2), HUT_SLEEP: True, HUT_NAME: u'Moonbeam Hut'},
                    {HUT_ARRIVAL: date(2013, 3, 3), HUT_SLEEP: True, HUT_NAME: u'Top Waitaha Hut'},
                    {HUT_ARRIVAL: date(2013, 3, 4), HUT_SLEEP: True, HUT_NAME: u'Ivory Lake Hut', HUT_MULTIPLE_NIGHTS: 2},
                    {HUT_ARRIVAL: date(2013, 3, 6), HUT_SLEEP: True, HUT_NAME: u'Top Tuke Hut'},
                    {HUT_ARRIVAL: date(2013, 3, 7), HUT_SLEEP: False, HUT_NAME: u'Dickie Spur Hut'},
                    {HUT_ARRIVAL: date(2013, 3, 7), HUT_SLEEP: True, HUT_NAME: u'Polluck Creek Hut'},
                    ]
    },
    {
        TRIP_START: date(2015, 3, 9),
        TRIP_END: date(2015, 3, 9),
        TRIP_DESC: 'Avalanche Peak dayhike',
        TRIP_REPORTS: ['https://www.facebook.com/mhhalverson/posts/10205236495125673'],
        TRIP_PARTY: ['Claire Woolf'],
    },
    {
        TRIP_START: date(2015, 3, 14),
        TRIP_END: date(2015, 3, 15),
        TRIP_DESC: 'Tongariro Great Walk',
        TRIP_REPORTS: ['https://www.facebook.com/mhhalverson/posts/10205338258029682',
                       'https://www.facebook.com/mhhalverson/posts/10205338317711174'],
        TRIP_PARTY: ['Claire Woolf', 'Ben Dunn'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2015, 3, 14), HUT_SLEEP: True, HUT_NAME: u'Mangatepopo Hut'},
                    {HUT_ARRIVAL: date(2015, 3, 15), HUT_SLEEP: False, HUT_NAME: u'Oturere Hut'},
                    {HUT_ARRIVAL: date(2015, 3, 15), HUT_SLEEP: False, HUT_NAME: u'Waihohonu Hut'},
                    ]
    },
    {
        TRIP_START: date(2015, 3, 18),
        TRIP_END: date(2015, 3, 20),
        TRIP_DESC: 'Lake Waikaremoana Great Walk',
        TRIP_REPORTS: ['https://www.facebook.com/mhhalverson/timeline/story?ut=60&wstart=1420099200&wend=1451635199&hash=-9086441183404781264&pagefilter=3',
                       'https://www.facebook.com/mhhalverson/posts/10205338436474143',
                       'https://www.facebook.com/mhhalverson/posts/10205338534636597',
                       'https://www.facebook.com/mhhalverson/posts/10205338602798301'],
        TRIP_PARTY: ['Claire Woolf', 'Dan Thorpe'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2015, 3, 18), HUT_SLEEP: True, HUT_NAME: u'Panekire Hut'},
                    {HUT_ARRIVAL: date(2015, 3, 19), HUT_SLEEP: False, HUT_NAME: u'Waiopaoa Hut'},
                    {HUT_ARRIVAL: date(2015, 3, 19), HUT_SLEEP: True, HUT_NAME: u'Marauiti Hut'},
                    {HUT_ARRIVAL: date(2015, 3, 20), HUT_SLEEP: False, HUT_NAME: u'Waiharuru Hut'},
                    {HUT_ARRIVAL: date(2015, 3, 20), HUT_SLEEP: False, HUT_NAME: u'Whanganui Hut'},
                    ]
    },
    # Urupukapuka Island (2018 Nov 17 - 18)
    {
        TRIP_START: date(2018, 11, 22),
        TRIP_END: date(2018, 11, 22),
        TRIP_DESC: 'Coromandel - Pinnacles',
        TRIP_REPORTS: ['https://www.facebook.com/mhhalverson/posts/10216010605471698'],
        TRIP_PARTY: ['Claire Woolf'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2018, 11, 22), HUT_SLEEP: False, HUT_NAME: u'Pinnacles Hut', HUT_REGION: 'Coromandel'},]
    },
    {
        TRIP_START: date(2018, 11, 30),
        TRIP_END: date(2018, 11, 30),
        TRIP_DESC: 'Mt Taranaki dayhike',
        TRIP_REPORTS: ['https://www.facebook.com/mhhalverson/posts/10216058013536870'],
        TRIP_PARTY: ['Claire Woolf'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2018, 11, 30), HUT_SLEEP: False, HUT_NAME: u'Maketawa Hut'},]
    },
    {
        TRIP_START: date(2018, 12, 2),
        TRIP_END: date(2018, 12, 4),
        TRIP_DESC: 'Whanganui Journey Great Walk',
        TRIP_REPORTS: ['https://www.facebook.com/mhhalverson/posts/10216058013536870'],
        TRIP_PARTY: ['Claire Woolf'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2018, 12, 2), HUT_SLEEP: True, HUT_NAME: u'John Coull Hut'},
                    {HUT_ARRIVAL: date(2018, 12, 3), HUT_SLEEP: True, HUT_NAME: u'Tīeke Marae/kāinga'},]
    },
    {
        TRIP_START: date(2018, 12, 5),
        TRIP_END: date(2018, 12, 7),
        TRIP_DESC: 'Ruahines - Longview Hut',
        TRIP_ABORTED: True,  # extreme winds, spent two nights in the hut as we Claire was a bit shell shocked from the ascent up the spur
        TRIP_REPORTS: ['https://www.facebook.com/mhhalverson/posts/10216128029367222'],
        TRIP_PARTY: ['Claire Woolf'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2018, 12, 5), HUT_SLEEP: True, HUT_NAME: u'Longview Hut', HUT_MULTIPLE_NIGHTS: 2},]
    },
    {
        TRIP_START: date(2018, 12, 8),
        TRIP_END: date(2018, 12, 12),
        TRIP_DESC: 'Tararua Middle Loop',
        TRIP_REPORTS: ['https://www.facebook.com/mhhalverson/posts/10216128029367222'],
        TRIP_PARTY: ['Claire Woolf'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2018, 12, 8), HUT_SLEEP: True, HUT_NAME: u'Waitewaewae Hut'},
                    {HUT_ARRIVAL: date(2018, 12, 9), HUT_SLEEP: True, HUT_NAME: u'Anderson Memorial Hut'},
                    {HUT_ARRIVAL: date(2018, 12, 10), HUT_SLEEP: True, HUT_NAME: u'Maungahuka Hut'},
                    {HUT_ARRIVAL: date(2018, 12, 11), HUT_SLEEP: True, HUT_NAME: u'Kime Hut'},
                    {HUT_ARRIVAL: date(2018, 12, 12), HUT_SLEEP: False, HUT_NAME: u'Field Hut'},
                    ]
    },
    {
        TRIP_START: date(2019, 1, 23),
        TRIP_END: date(2019, 1, 24),
        TRIP_DESC: 'Ōtamahua/Quail Island',
        TRIP_REPORTS: ['https://drive.google.com/drive/folders/1-3WmupKlY8ad-YII4BXDRKGWP--kR1ae'],
        TRIP_PARTY: ['Claire Woolf',
                     'Dave Manning', 'Sophie Manning', 'Luca Manning',
                     'Lindsey Alton', 'Ivor Heijnen', 'Ashleigh Alton',
                     'Sam Kipling', 'Sophie Kipling', 'Anna Cousins', 'Nate Cousins'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2019, 1, 23), HUT_SLEEP: True, HUT_NAME: 'Ōtamahua Hut'}],
    },
    {
        TRIP_START: date(2019, 3, 2),
        TRIP_END: date(2019, 3, 3),
        TRIP_DESC: 'Tara Tama',
        TRIP_ABORTED: True,  # I was feeling sick and threw up multiple times. Dave gave me all his water and I camped on the ridge and didn't actually go up to Tara Tama.
        TRIP_REPORTS: ['https://www.facebook.com/ivor.heijnen/posts/10157178046720908'],
        TRIP_PARTY: ['Dave Manning', 'Ivor Heijnen'],
    },
    {
        TRIP_START: date(2019, 4, 25),
        TRIP_END: date(2019, 4, 25),
        TRIP_DESC: 'Mt Somers',
        # TRIP_REPORTS: [''], # TODO post my photos
        TRIP_PARTY: ['Dave Manning'],
    },

     {
         TRIP_START: date(2019, 6, 29),
         TRIP_END: date(2019, 6, 30),
         TRIP_DESC: 'Avoca Hut - Jordan / Sphinx',
         # TRIP_REPORTS: [''], # TODO post my photos
         TRIP_PARTY: ['Dave Manning'],
         TRIP_HUTS: [{HUT_ARRIVAL: date(2019, 6, 29), HUT_SLEEP: True, HUT_NAME: u'Avoca Hut'},
                     {HUT_ARRIVAL: date(2019, 6, 30), HUT_SLEEP: False, HUT_NAME: u'Anti Crow Hut'},]
     },

     {
         TRIP_START: date(2019, 9, 8),
         TRIP_END: date(2019, 9, 9),
         TRIP_DESC: 'Welcome Flat',
         TRIP_REPORTS: ['https://www.facebook.com/photo/?fbid=10157426862991904&set=t.1045230044'], # TODO post my photos too
         TRIP_PARTY: ['Claire Woolf', 'Derek Pell', 'Audrey Vorametsanti'],
         TRIP_HUTS: [{HUT_ARRIVAL: date(2019, 9, 8), HUT_SLEEP: True, HUT_NAME: u'Welcome Flat Hut'},]
     },

     {
         TRIP_START: date(2019, 12, 7),
         TRIP_END: date(2019, 12, 8),
         TRIP_DESC: 'Pigeon Bay camping',
         # TRIP_REPORTS: [''], # TODO post my photos
         TRIP_PARTY: ['Claire Woolf', 'Alison Tang', 'Michael Coe'], # and a few others
     },

     {
         TRIP_START: date(2020, 1, 11),
         TRIP_END: date(2020, 1, 12),
         TRIP_DESC: 'Mt Kerr/Lower Olderog',
         # TRIP_REPORTS: [''], # TODO post my photos
         TRIP_PARTY: ['Dave Manning', 'Ivor Heijnen'],
         TRIP_HUTS: [{HUT_ARRIVAL: date(2020, 1, 11), HUT_SLEEP: True, HUT_NAME: u'Lower Olderog Bivvy'},]
     },

     {
         TRIP_START: date(2020, 2, 6),
         TRIP_END: date(2020, 2, 9),
         TRIP_DESC: 'Hope/Doubtful/Nina over Waitangi',
         # TRIP_REPORTS: [''], # TODO post my photos
         TRIP_PARTY: ['Claire Woolf', 'Melanie LaPointe'],
         TRIP_HUTS: [{HUT_ARRIVAL: date(2020, 2, 6), HUT_SLEEP: False, HUT_NAME: u'Hope Halfway Hut'},
                     {HUT_ARRIVAL: date(2020, 2, 6), HUT_SLEEP: True, HUT_NAME: u"St Jacob's Hut"},
                     {HUT_ARRIVAL: date(2020, 2, 7), HUT_SLEEP: False, HUT_NAME: u'Lake Man Bivvy'},
                     {HUT_ARRIVAL: date(2020, 2, 7), HUT_SLEEP: True, HUT_NAME: u'Doubtless Hut'},
                     {HUT_ARRIVAL: date(2020, 2, 8), HUT_SLEEP: False, HUT_NAME: u'Doubtful Hut'},
                     {HUT_ARRIVAL: date(2020, 2, 8), HUT_SLEEP: False, HUT_NAME: u'Devils Den Bivvy'},
                     {HUT_ARRIVAL: date(2020, 2, 8), HUT_SLEEP: True, HUT_NAME: u'Nina Hut'},]
     },

     {
         TRIP_START: date(2020, 5, 1),
         TRIP_END: date(2020, 5, 1),
         TRIP_DESC: 'Mt Herbert',
         # TRIP_REPORTS: [''], # TODO post my photos too
         TRIP_PARTY: ['Claire Woolf'],
     },

     {
         TRIP_START: date(2020, 5, 30),
         TRIP_END: date(2020, 5, 31),
         TRIP_DESC: "Dave's first tramp - reprise",
         TRIP_REPORTS: ['https://www.facebook.com/photo/?fbid=10158489213023126&set=t.1045230044'], # TODO post my photos too
         TRIP_PARTY: ['Dave Manning', 'Ivor Heijnen'],
         TRIP_HUTS: [{HUT_ARRIVAL: date(2020, 5, 30), HUT_SLEEP: False, HUT_NAME: u'Brass Monkey Bivvy'},
                     {HUT_ARRIVAL: date(2020, 5, 30), HUT_SLEEP: False, HUT_NAME: u'Lake Christabel Hut'},
                     {HUT_ARRIVAL: date(2020, 5, 31), HUT_SLEEP: False, HUT_NAME: u'Upper Nina Bivvy'},]
     },

     {
         TRIP_START: date(2020, 8, 21),
         TRIP_END: date(2020, 8, 21),
         TRIP_DESC: 'Kaituna Grande Loop',
         TRIP_REPORTS: ['https://www.strava.com/activities/3943347600'],
         TRIP_PARTY: ['Brian Thorne', 'Lindsey Alton'],
         TRIP_HUTS: [{HUT_ARRIVAL: date(2020, 8, 21), HUT_SLEEP: False, HUT_NAME: u'Packhorse Hut'},]
     },

     {
         TRIP_START: date(2020, 8, 22),
         TRIP_END: date(2020, 8, 23),
         TRIP_DESC: 'Bealey Spur amble',
         # TRIP_REPORTS: [''], # TODO post my photos
         TRIP_PARTY: ['Claire Woolf', 'Dave Manning', 'Sophie Manning', 'Luca Manning'],
     },

     {
         TRIP_START: date(2020, 9, 12),
         TRIP_END: date(2020, 9, 12),
         TRIP_DESC: 'Mt Bealey / Avalanche Peak',
         TRIP_REPORTS: ['https://www.facebook.com/mhhalverson/posts/10221460310310913'],
         TRIP_PARTY: ['Ivor Heijnen'],
     },

     {
         TRIP_START: date(2020, 9, 27),
         TRIP_END: date(2020, 9, 30),
         TRIP_DESC: 'Heaphy Track',
         TRIP_REPORTS: ['https://photos.google.com/share/AF1QipM97c2HETJU2hI4KFcYN32lLDcnA5emhfaHYiKS5YsOnLcOlj8W4wwdiPZ1eISA9g?key=eUpUTmdHdm8ySXMtUVo2SEpyMjlGVHctS1pQMUV3'],
         TRIP_PARTY: ['Claire Woolf', 'Kirstie McHale', 'Alison Tang', 'Emma Gavenda'],
         TRIP_HUTS: [{HUT_ARRIVAL: date(2020, 9, 27), HUT_SLEEP: False, HUT_NAME: u'Brown Hut', HUT_REGION: 'Nelson/Tasman'},
                     {HUT_ARRIVAL: date(2020, 9, 27), HUT_SLEEP: True, HUT_NAME: u'Perry Saddle Hut'},
                     {HUT_ARRIVAL: date(2020, 9, 28), HUT_SLEEP: False, HUT_NAME: u'Gouland Downs Hut'},
                     {HUT_ARRIVAL: date(2020, 9, 28), HUT_SLEEP: False, HUT_NAME: u'Saxon Hut'},
                     {HUT_ARRIVAL: date(2020, 9, 28), HUT_SLEEP: True, HUT_NAME: u'James Mackay Hut'},
                     {HUT_ARRIVAL: date(2020, 9, 29), HUT_SLEEP: False, HUT_NAME: u'Lewis Hut'},
                     {HUT_ARRIVAL: date(2020, 9, 29), HUT_SLEEP: True, HUT_NAME: u'Heaphy Hut'},]
     },

     {
         TRIP_START: date(2020, 10, 2),
         TRIP_END: date(2020, 10, 5),
         TRIP_DESC: 'Abel Tasman Coast Track',
         TRIP_REPORTS: ['https://photos.google.com/share/AF1QipMsc7XLeuUwGCqMKlPjw3NhuMRZB29EET0DWilKESzmze5CE3xDrcYVXOYaPxjaLQ?key=a245WTBxT0h5OTdTT0xVTGlQMUZPcDBEOUpIMnhR'],
         TRIP_PARTY: ['Claire Woolf', 'Stan Klevtsov', 'Alison Tang', 'Michael Coe'],
         TRIP_HUTS: [{HUT_ARRIVAL: date(2020, 10, 2), HUT_SLEEP: True, HUT_NAME: u'Whariwharangi Hut'},
                     {HUT_ARRIVAL: date(2020, 10, 3), HUT_SLEEP: True, HUT_NAME: u'Awaroa Hut'},
                     {HUT_ARRIVAL: date(2020, 10, 4), HUT_SLEEP: True, HUT_NAME: u'Bark Bay Hut'},]
     },

     {
         TRIP_START: date(2020, 10, 17),
         TRIP_END: date(2020, 10, 18),
         TRIP_DESC: 'Ōtamahua/Quail Island',
         TRIP_REPORTS: ['https://photos.google.com/share/AF1QipP5JBd7LfTYT-W4s1PYUWITEqLdgdw0_t6dHl2FfjF8PhuyQAjA52wBZbcRsF7HqA?key=UnVEWGg4UGVqNXg5b0VVaTB6Y0dzS1V5dld0UU1R&pli=1'],
         TRIP_PARTY: ['Claire Woolf', 'Heather Penzel', 'Eve Russell',
                     'Dave Manning', 'Sophie Manning', 'Luca Manning',
                     'Lindsey Alton', 'Ashleigh Alton',
                     'Brian Thorne', 'Sarah Thorne', 'Juliet Thorne', 'Frederick Thorne'],
         TRIP_HUTS: [{HUT_ARRIVAL: date(2020, 10, 17), HUT_SLEEP: True, HUT_NAME: u'Ōtamahua Hut'},],
     },

     {
         TRIP_START: date(2020, 12, 5),
         TRIP_END: date(2020, 12, 5),
         TRIP_DESC: 'Kepler Challenge 2020',
         TRIP_REPORTS: [
             'https://www.facebook.com/mhhalverson/posts/10222091021958310',
             'https://matthalverson.com/2020/12/23/running.html',
         ],
         TRIP_PARTY: ['Sarah Bouckoms', 'Curtis Moore', 'Bev Thorne'],
         TRIP_HUTS: [{HUT_ARRIVAL: date(2020, 12, 5), HUT_SLEEP: False, HUT_NAME: u'Luxmore Hut'},
                     {HUT_ARRIVAL: date(2020, 12, 5), HUT_SLEEP: False, HUT_NAME: u'Moturau Hut'},],
     },

     {
         TRIP_START: date(2020, 12, 14),
         TRIP_END: date(2020, 12, 15),
         TRIP_DESC: 'Milford Track / Dore Pass',
         TRIP_REPORTS: [
             'https://photos.app.goo.gl/Ymij1TVXSC8CNZd87',
             'https://matthalverson.com/2020/12/23/running.html',
             ],
         TRIP_PARTY: ['Lindsey Alton', 'Ivor Heijnen'],
         TRIP_HUTS: [{HUT_ARRIVAL: date(2020, 12, 14), HUT_SLEEP: False, HUT_NAME: u'Dumpling Hut'},
                     {HUT_ARRIVAL: date(2020, 12, 14), HUT_SLEEP: False, HUT_NAME: u'Mintaro Hut'},
                     {HUT_ARRIVAL: date(2020, 12, 14), HUT_SLEEP: False, HUT_NAME: u'Clinton Hut'},],
     },

     {
         TRIP_START: date(2020, 12, 27),
         TRIP_END: date(2020, 12, 27),
         TRIP_DESC: 'Gertrude Saddle',
         TRIP_REPORTS: [
             'https://photos.google.com/share/AF1QipN2NCUMc5L6GhiSNqmsXbNBlh6fliKcMxgCwM8KuhtIo577-e8LiKFpat_cbuKf1w',
             # TODO add my own link
             ],
         TRIP_PARTY: ['Brian Thorne', 'Sarah Thorne', 'Neville Thorne', 'Douglas Thorne', 'Jessica Thorne', 'Claire Woolf'],
     },

     {
         TRIP_START: date(2020, 12, 29),
         TRIP_END: date(2021, 1, 2),
         TRIP_DESC: 'Stewart Island Southern Circuit',
         TRIP_ABORTED: True,  # Claire was feeling extremely low energy so we turned back after the first day
         # TRIP_REPORTS: [''], # TODO post my photos
         TRIP_PARTY: ['Claire Woolf'],
         TRIP_HUTS: [{HUT_ARRIVAL: date(2020, 12, 29), HUT_SLEEP: True, HUT_NAME: u'Freds Camp Hut'},
                     {HUT_ARRIVAL: date(2020, 12, 30), HUT_SLEEP: True, HUT_NAME: u'Rakeahua Hut'},
                     {HUT_ARRIVAL: date(2020, 12, 31), HUT_SLEEP: True, HUT_NAME: u'Freds Camp Hut'},
                     {HUT_ARRIVAL: date(2021, 1, 1), HUT_SLEEP: True, HUT_NAME: u'Freds Camp Hut'},],
     },

     {
         TRIP_START: date(2021, 1, 9),
         TRIP_END: date(2021, 1, 9),
         TRIP_DESC: 'Goat Pass',
         # TRIP_REPORTS: [''], # TODO post my photos
         TRIP_PARTY: ['Neil Campbell', 'Katherine Lydiard', 'Craig Muir', 'Reuben Costello'], # also Katherine's friend Phil.
         TRIP_HUTS: [{HUT_ARRIVAL: date(2021, 1, 9), HUT_SLEEP: False, HUT_NAME: u'Upper Deception Hut'},
                     {HUT_ARRIVAL: date(2021, 1, 9), HUT_SLEEP: False, HUT_NAME: u'Goat Pass Hut'},
                     {HUT_ARRIVAL: date(2021, 1, 9), HUT_SLEEP: False, HUT_NAME: u'Mingha Bivvy'},],
     },

     {
         TRIP_START: date(2021, 1, 22),
         TRIP_END: date(2021, 1, 24),
         TRIP_DESC: 'Summit Walkway',
         # TRIP_REPORTS: [''], # TODO post my photos
         TRIP_PARTY: ['Claire Woolf', 'Kirstie McHale', 'Arthur Gordon-Wright', 'Thomas Caspari', 'Nina Koele', 'Brian Thorne', 'Juliet Thorne'],
         TRIP_HUTS: [{HUT_ARRIVAL: date(2021, 1, 22), HUT_SLEEP: True, HUT_NAME: u'Packhorse Hut'},
                     {HUT_ARRIVAL: date(2021, 1, 23), HUT_SLEEP: True, HUT_NAME: u'Rod Donald Hut'}],
     },

     {
         TRIP_START: date(2021, 2, 20),
         TRIP_END: date(2021, 2, 21),
         TRIP_DESC: 'Mt Brown Hut',
         # TRIP_REPORTS: [''], # TODO post my photos
         TRIP_PARTY: ['Dave Manning', 'Pete Russell'],
         TRIP_HUTS: [{HUT_ARRIVAL: date(2021, 2, 20), HUT_SLEEP: True, HUT_NAME: u'Mt Brown Hut'}],
     },

    {
        TRIP_START: date(2021, 4, 4),
        TRIP_END: date(2021, 4, 4),
        TRIP_DESC: 'Lucretia Biv Reno',
        # TRIP_REPORTS: [''], # TODO post my photos
        TRIP_PARTY: ['Lindsey Alton', 'Ivor Heijnen', 'Ashleigh Alton'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2021, 4, 4), HUT_SLEEP: True, HUT_NAME: u'Lucretia Hut'},],
    },

    {
        TRIP_START: date(2021, 4, 9),
        TRIP_END: date(2021, 4, 10),
        TRIP_DESC: 'Old Ghost Road',
        # TRIP_REPORTS: [''], # TODO post my photos
        TRIP_PARTY: ['Dave Manning', 'Damian Philipsen'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2021, 4, 9), HUT_SLEEP: False, HUT_NAME: u'Lyell Saddle Hut'},
                    {HUT_ARRIVAL: date(2021, 4, 9), HUT_SLEEP: True, HUT_NAME: u'Ghost Lake Hut'},
                    {HUT_ARRIVAL: date(2021, 4, 10), HUT_SLEEP: False, HUT_NAME: u'Stern Valley Hut'},
                    {HUT_ARRIVAL: date(2021, 4, 10), HUT_SLEEP: False, HUT_NAME: u'Mokihinui Forks Hut'},
                    {HUT_ARRIVAL: date(2021, 4, 10), HUT_SLEEP: False, HUT_NAME: u'Goat Creek Hut'},
                    {HUT_ARRIVAL: date(2021, 4, 10), HUT_SLEEP: False, HUT_NAME: u'Specimen Point Hut'},]
    },

    {
        TRIP_START: date(2021, 10, 22),
        TRIP_END: date(2021, 10, 24),
        TRIP_DESC: 'Mt Owen and surrounds',
        # TRIP_REPORTS: [''], # TODO post my photos
        TRIP_PARTY: ['Wouter van Beerschoten'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2021, 10, 23), HUT_SLEEP: True, HUT_NAME: u'Granity Pass Hut',},]
    },

    {
        TRIP_START: date(2021, 11, 12),
        TRIP_END: date(2021, 11, 12),
        TRIP_DESC: 'Mt Fyffe run',
        TRIP_REPORTS: ['https://www.strava.com/activities/6245917387'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2021, 11, 12), HUT_SLEEP: False, HUT_NAME: u'Mt Fyffe Hut',},]
    },

    {
         TRIP_START: date(2021, 1, 15),
         TRIP_END: date(2021, 1, 15),
         TRIP_DESC: 'Kepler Challenge 2021 (2022)',
         TRIP_REPORTS: [
             'https://www.facebook.com/mhhalverson/posts/pfbid038DYgeP21ksnEGcdqYwncxBtEyJZo7BCoygnm2rAMF9apWjBPTaufpfW7x5fBpAQMl',
             'https://www.strava.com/activities/6535272146',
         ],
         TRIP_PARTY: ['Christian Ruegg', 'Neville Thorne', 'Bev Thorne'],
         TRIP_HUTS: [{HUT_ARRIVAL: date(2021, 1, 15), HUT_SLEEP: False, HUT_NAME: u'Luxmore Hut'},
                     {HUT_ARRIVAL: date(2021, 1, 15), HUT_SLEEP: False, HUT_NAME: u'Iris Burn Hut'},
                     {HUT_ARRIVAL: date(2021, 1, 15), HUT_SLEEP: False, HUT_NAME: u'Moturau Hut'},],
     },

    {
        TRIP_START: date(2022, 2, 18),
        TRIP_END: date(2022, 2, 18),
        TRIP_DESC: 'Old Ghost Ultra (DIY)',
        TRIP_REPORTS: ['https://www.strava.com/activities/6700398178'],
        TRIP_PARTY: ['Mark Hebberd', 'Mike McManaway'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2022, 4, 18), HUT_SLEEP: False, HUT_NAME: u'Specimen Point Hut'},
                    {HUT_ARRIVAL: date(2022, 2, 18), HUT_SLEEP: False, HUT_NAME: u'Goat Creek Hut'},
                    {HUT_ARRIVAL: date(2022, 2, 18), HUT_SLEEP: False, HUT_NAME: u'Mokihinui Forks Hut'},
                    {HUT_ARRIVAL: date(2022, 2, 18), HUT_SLEEP: False, HUT_NAME: u'Stern Valley Hut'},
                    {HUT_ARRIVAL: date(2022, 2, 18), HUT_SLEEP: False, HUT_NAME: u'Ghost Lake Hut'},
                    {HUT_ARRIVAL: date(2022, 2, 18), HUT_SLEEP: False, HUT_NAME: u'Lyell Saddle Hut'},],
    },

    {
        TRIP_START: date(2022, 3, 19),
        TRIP_END: date(2022, 3, 19),
        TRIP_DESC: 'Diamond in the Rough',
        TRIP_REPORTS: ['https://www.strava.com/activities/6846203113'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2022, 3, 19), HUT_SLEEP: False, HUT_NAME: u'Sylvester Hut'},],
    },

    {
        TRIP_START: date(2022, 3, 20),
        TRIP_END: date(2022, 3, 20),
        TRIP_DESC: 'The Rameka to Pigeon Dance',
        TRIP_REPORTS: ['https://www.strava.com/activities/6851363451'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2022, 3, 20), HUT_SLEEP: False, HUT_NAME: u'Wainui Hut',},
                    {HUT_ARRIVAL: date(2022, 3, 20), HUT_SLEEP: False, HUT_NAME: u'Awapoto Hut'},]
    },

    {
        TRIP_START: date(2022, 4, 23),
        TRIP_END: date(2022, 4, 24),
        TRIP_DESC: 'Lake Man via Doubtful Tops',
        TRIP_REPORTS: ['https://matthalverson.com/2022/05/16/doubtful-tops.html'],
        TRIP_PARTY: ['Dave Manning', 'Pete Russell'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2022, 4, 23), HUT_SLEEP: True, HUT_NAME: u'Lake Man Bivvy',},
                    {HUT_ARRIVAL: date(2022, 4, 24), HUT_SLEEP: False, HUT_NAME: u'Doubtful Hut'},]
    },

    {
        TRIP_START: date(2022, 6, 18),
        TRIP_END: date(2022, 6, 18),
        TRIP_DESC: 'Bealey Spur',
        # TRIP_REPORTS: [''], # TODO post my photos
        TRIP_PARTY: ['Sophie Manning'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2022, 6, 18), HUT_SLEEP: False, HUT_NAME: u'Bealey Spur Hut',},]
    },

    {
        TRIP_START: date(2022, 6, 25),
        TRIP_END: date(2022, 6, 26),
        TRIP_DESC: 'Mt Fyffe Cheesefest',
        # TRIP_REPORTS: [''], # TODO post my photos
        TRIP_PARTY: ['Christian Ruegg', 'Neil Whiteside', 'Lyndsay Fenn'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2022, 6, 25), HUT_SLEEP: True, HUT_NAME: u'Mt Fyffe Hut',},]
    },

    {
        TRIP_START: date(2022, 10, 9),
        TRIP_END: date(2022, 10, 9),
        TRIP_DESC: 'Cass-Lagoon run',
        TRIP_REPORTS: ['https://www.strava.com/activities/7933856916'],
        TRIP_PARTY: ['Christian Ruegg', 'Dylan Steeples'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2022, 10, 9), HUT_SLEEP: False, HUT_NAME: u'Bealey Hut',},
                    {HUT_ARRIVAL: date(2022, 10, 9), HUT_SLEEP: False, HUT_NAME: u'Lagoon Saddle A Frame Hut',},
                    {HUT_ARRIVAL: date(2022, 10, 9), HUT_SLEEP: False, HUT_NAME: u'Lagoon Saddle Hut',},
                    {HUT_ARRIVAL: date(2022, 10, 9), HUT_SLEEP: False, HUT_NAME: u'West Harper Hut',},
                    {HUT_ARRIVAL: date(2022, 10, 9), HUT_SLEEP: False, HUT_NAME: u'Hamilton Hut',},
                    {HUT_ARRIVAL: date(2022, 10, 9), HUT_SLEEP: False, HUT_NAME: u'Cass Saddle Hut',}, ]
    },

    {
        TRIP_START: date(2022, 12, 3),
        TRIP_END: date(2022, 12, 3),
        TRIP_DESC: 'Kepler Challenge 2022',
        TRIP_REPORTS: ['https://www.strava.com/activities/8199892980',
            'https://www.facebook.com/mhhalverson/posts/pfbid05zmKARKY71UKd6dymQqYqEaG37tqdTqsVa68jXwWincpkvuNNJ1i97Tc7JJB2vzWl',
            'https://www.facebook.com/christian.eriounes/posts/pfbid02ZQkeWby4y54s2bc6tchJcamLmbdddR5q8NaKUf2WksGsUcU4UHLq9wDkdmpun8nGl',
            'https://www.facebook.com/sarah.antarctica.9/posts/pfbid027WtvBWrQ2XTMrsYnFMTzZQLMyAwgH3VLrFBUuEbbjvEk7CKmTZz7RUvmhpAJ5c4Pl'],
        TRIP_PARTY: ['Christian Ruegg', 'Sarah Bouckoms', 'Hector Plaza', 'Bev Thorne', 'Kevin Grimwood', 'Tim Ensor'],
         TRIP_HUTS: [{HUT_ARRIVAL: date(2022, 12, 3), HUT_SLEEP: False, HUT_NAME: u'Luxmore Hut'},
                     {HUT_ARRIVAL: date(2022, 12, 3), HUT_SLEEP: False, HUT_NAME: u'Iris Burn Hut'},
                     {HUT_ARRIVAL: date(2022, 12, 3), HUT_SLEEP: False, HUT_NAME: u'Moturau Hut'},],
    },

    {
        TRIP_START: date(2022, 12, 9),
        TRIP_END: date(2022, 12, 10),
        TRIP_DESC: "Rod Donald Hut for Kirstie's birthday",
        TRIP_REPORTS: ['https://www.strava.com/activities/8229537220'],
        TRIP_PARTY: ['Claire Woolf', 'Jamie Halverson', 'Kirstie McHale', 'Arthur Gordon-Wright', 'Cecile Bourgignon', 'Eli Wolff', 'Ashlee', 'Brian Thorne', 'Sarah Thorne', 'Juliet Thorne', 'Frederick Thorne'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2022, 12, 9), HUT_SLEEP: True, HUT_NAME: u'Rod Donald Hut'},],
    },

    {
        TRIP_START: date(2023, 1, 26),
        TRIP_END: date(2023, 1, 28),
        TRIP_DESC: 'Routeburn',
        # TRIP_REPORTS: [''], # TODO post my photos
        TRIP_PARTY: ['Claire Woolf', 'Jamie Halverson', 'Bev Thorne', 'Brian Thorne', 'Sarah Thorne', 'Juliet Thorne', 'Frederick Thorne', 'Alison Tang', 'Michael Coe', 'Kirstie McHale'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2023, 1, 26), HUT_SLEEP: False, HUT_NAME: u'Lake Mackenzie Hut'},
                    {HUT_ARRIVAL: date(2023, 1, 27), HUT_SLEEP: False, HUT_NAME: u'Routeburn Falls Hut'},
                    {HUT_ARRIVAL: date(2023, 1, 27), HUT_SLEEP: False, HUT_NAME: u'Routeburn Flats Hut'},]
    },

    {
        TRIP_START: date(2023, 2, 12),
        TRIP_END: date(2023, 2, 13),
        TRIP_DESC: 'Inland Pack Track',
        TRIP_REPORTS: ['https://www.strava.com/activities/8551935474',
            'https://www.strava.com/activities/8551936936',
            'https://www.strava.com/activities/8578539877'],
        TRIP_PARTY: ['Claire Woolf', 'Jamie Halverson'],
    },

    {
        TRIP_START: date(2023, 4, 15),
        TRIP_END: date(2023, 4, 15),
        TRIP_DESC: 'Mt Oxford Odyssey',
        TRIP_REPORTS: ['https://www.strava.com/activities/8892397218'],
        TRIP_PARTY: ['Jeremy Wheeler', 'Iain Gover'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2023, 4, 15), HUT_SLEEP: False, HUT_NAME: u'Wharfedale Hut'},
                    {HUT_ARRIVAL: date(2023, 4, 15), HUT_SLEEP: False, HUT_NAME: u'Black Hill Hut'},]
    },

    {
        TRIP_START: date(2023, 9, 10),
        TRIP_END: date(2023, 9, 10),
        TRIP_DESC: 'Tribulation / Cookies',
        TRIP_REPORTS: ['https://www.strava.com/activities/9818225060'],
        TRIP_PARTY: [], # solo
        TRIP_HUTS: [{HUT_ARRIVAL: date(2023, 9, 10), HUT_SLEEP: False, HUT_NAME: u'Tribulation Hut'},
                    {HUT_ARRIVAL: date(2023, 9, 10), HUT_SLEEP: False, HUT_NAME: u'Cookies Hut'},]
    },

    {
        TRIP_START: date(2023, 10, 21),
        TRIP_END: date(2023, 10, 21),
        TRIP_DESC: 'Hawdon-Edwards Classic',
        TRIP_REPORTS: ['https://www.strava.com/activities/10075005674'],
        TRIP_PARTY: [], # solo
        TRIP_HUTS: [{HUT_ARRIVAL: date(2023, 10, 21), HUT_SLEEP: False, HUT_NAME: u'Hawdon Hut'},
                    {HUT_ARRIVAL: date(2023, 10, 21), HUT_SLEEP: False, HUT_NAME: u'Edwards Hut'},]
    },

    {
        TRIP_START: date(2023, 12, 18),
        TRIP_END: date(2023, 12, 20),
        TRIP_DESC: 'Hump Ridge',
        # TRIP_REPORTS: [''], # TODO post my photos
        TRIP_PARTY: ['Claire Woolf', 'Jamie Halverson'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2023, 12, 19), HUT_SLEEP: False, HUT_NAME: u'Port Craig School Hut'},]
    },

    {
        TRIP_START: date(2024, 7, 20),
        TRIP_END: date(2024, 7, 21),
        TRIP_DESC: 'Glenrae Hut',
        TRIP_REPORTS: ['https://www.strava.com/activities/11941173899',
                       'https://www.strava.com/activities/11941193678'],
        TRIP_PARTY: ['Dave Manning'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2024, 7, 20), HUT_SLEEP: True, HUT_NAME: u'Glenrae Hut'},
                    {HUT_ARRIVAL: date(2024, 7, 21), HUT_SLEEP: False, HUT_NAME: u'Cold Stream Hut'},]
    },

    {
        TRIP_START: date(2024, 9, 14),
        TRIP_END: date(2024, 9, 14),
        TRIP_DESC: 'Lees Valley',
        TRIP_REPORTS: ['https://www.strava.com/activities/12404430222'],
        TRIP_PARTY: ['Christian Ruegg'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2024, 9, 14), HUT_SLEEP: False, HUT_NAME: u'Youngman Stream Hut'},
                    {HUT_ARRIVAL: date(2024, 9, 14), HUT_SLEEP: False, HUT_NAME: u'Tarn Hut', HUT_REGION: 'Canterbury'},]
    },

    # {
    #     TRIP_START: date(2024, ),
    #     TRIP_END: date(2024, ),
    #     TRIP_DESC: '',
    #     TRIP_ABORTED: True,
    #     TRIP_REPORTS: [''],
    #     TRIP_PARTY: [],
    #     TRIP_HUTS: [{HUT_ARRIVAL: date(2024, ), HUT_SLEEP: , HUT_NAME: u'', HUT_REGION: '', HUT_IS_DOC_MAINTAINED: False, HUT_MULTIPLE_NIGHTS: 2},
    #                 {HUT_ARRIVAL: date(2024, ), HUT_SLEEP: , HUT_NAME: u''},]
    # },

]

class Trip(object):
    @classmethod
    def from_dict(cls, dict_):
        t = cls()
        t.start = dict_[TRIP_START]
        t.end = dict_[TRIP_END]
        t.desc = dict_[TRIP_DESC]
        t.party = tuple(dict_.get(TRIP_PARTY, ["don't remember"]))
        t.aborted = dict_.get(TRIP_ABORTED, False)
        t.reports = tuple(dict_.get(TRIP_REPORTS, []))
        t.hut_visits = tuple([HutVisit.from_dict(hv) for hv in dict_.get(TRIP_HUTS, [])])
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
        hv.num_days = dict_.get(HUT_MULTIPLE_NIGHTS, 1)
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
