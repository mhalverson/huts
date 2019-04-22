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
        TRIP_START: date(2019, ),
        TRIP_END: date(2019, ),
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
                    {HUT_ARRIVAL: date(2010, 8, 23), HUT_SLEEP: False, HUT_NAME: u'Murray Hunters Hut'},
                    {HUT_ARRIVAL: date(2010, 8, 23), HUT_SLEEP: False, HUT_NAME: u'Christmas Village Hunters Hut - 2017'},
                    {HUT_ARRIVAL: date(2010, 8, 23), HUT_SLEEP: True, HUT_NAME: u'Christmas Village Hut'},
                    {HUT_ARRIVAL: date(2010, 8, 24), HUT_SLEEP: True, HUT_NAME: u'Yankee River Hut'},
                    {HUT_ARRIVAL: date(2010, 8, 25), HUT_SLEEP: False, HUT_NAME: u'Smoky Hunters Hut'},
                    {HUT_ARRIVAL: date(2010, 8, 25), HUT_SLEEP: False, HUT_NAME: u'Long Harry Hut'},
                    {HUT_ARRIVAL: date(2010, 8, 25), HUT_SLEEP: True, HUT_NAME: u'East Ruggedy Hut', HUT_MULTIPLE_NIGHTS: 2},
                    {HUT_ARRIVAL: date(2010, 8, 27), HUT_SLEEP: True, HUT_NAME: u'Big Hellfire Hut'},
                    {HUT_ARRIVAL: date(2010, 8, 28), HUT_SLEEP: True, HUT_NAME: u'Mason Bay Hut'},
                    {HUT_ARRIVAL: date(2010, 8, 29), HUT_SLEEP: False, HUT_NAME: u'Homestead Hunters Hut'},
                    {HUT_ARRIVAL: date(2010, 8, 29), HUT_SLEEP: True, HUT_NAME: u'Freshwater Hut'},
                    {HUT_ARRIVAL: date(2010, 8, 30), HUT_SLEEP: False, HUT_NAME: u'North Arm Hut'},
                    ]
    },
    # Hollyford UCCC trip (2010 Sep ?2? - ?4?) https://www.facebook.com/mhhalverson/media_set?set=a.1554515216549&type=3
    # (failed) Lake Man Biv (2010 Sep 13 - 14) none, Sophie and I just camped in the shelter at the road-end :)
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
        TRIP_ABORTED: True,
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
                    {HUT_ARRIVAL: date(2018, 12, 3), HUT_SLEEP: True, HUT_NAME: u'Tieke Kainga'},]
    },
    {
        TRIP_START: date(2018, 12, 5),
        TRIP_END: date(2018, 12, 7),
        TRIP_DESC: 'Ruahines - Longview Hut',
        TRIP_ABORTED: True,
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
                    {HUT_ARRIVAL: date(2018, 12, 12), HUT_SLEEP: False, HUT_NAME: u'Field Hut (Historic)'},
                    ]
    },
    {
        TRIP_START: date(2019, 1, 23),
        TRIP_END: date(2019, 1, 24),
        TRIP_DESC: 'Ōtamahua/Quail Island',
        TRIP_REPORTS: ['https://drive.google.com/drive/folders/1-3WmupKlY8ad-YII4BXDRKGWP--kR1ae'],
        TRIP_PARTY: ['Dave Manning', 'Sophie Manning', 'Luca Manning',
                     'Lindsey Alton', 'Ivor Heijnen', 'Ashleigh Alton',
                     'Sam Kipling', 'Sophie Kipling', 'Anna Cousins', 'Nate Cousins'],
        TRIP_HUTS: [{HUT_ARRIVAL: date(2019, 1, 23), HUT_SLEEP: True, HUT_NAME: 'Ōtamahua Hut'}],
    },
    {
        TRIP_START: date(2019, 3, 2),
        TRIP_END: date(2019, 3, 3),
        TRIP_DESC: 'Tara Tama',
        TRIP_ABORTED: True,  # I camped on the ridge and didn't actually go up to Tara Tama
        TRIP_REPORTS: ['https://www.facebook.com/ivor.heijnen/posts/10157178046720908'],
        TRIP_PARTY: ['Dave Manning', 'Ivor Heijnen'],
    },
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
