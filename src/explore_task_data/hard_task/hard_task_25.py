stage_data = {
    '25-1-sss-present-task': {
        'start': [
            ['shock1', (784, 217)],
            ['pierce1', (479, 621)],
        ],
        'action': [
            {'t': 'click', 'p': (656, 368), 'ec': True, 'desc': "1 lower left"},
            {'t': 'click', 'p': (625, 409), 'ec': True, 'wait-over': True, 'desc': "2 upper right"},

            {'t': 'click', 'p': (654, 371), 'ec': True, 'desc': "1 lower left"},
            {'t': 'choose_and_change', 'p': (654, 371), 'desc': "swap 1 2"},
            {'t': 'click', 'p': (597, 287), 'ec': True, 'wait-over': True, 'desc': "2 upper left"},

            {'t': 'click', 'p': (711, 455), 'ec': True, 'desc': "1 right"},
            {'t': 'click', 'p': (541, 205), 'ec': True, 'wait-over': True, 'desc': "2 upper left"},

            {'t': 'click', 'p': (740, 422), 'ec': True, 'desc': "1 right"},
            {'t': 'click', 'p': (439, 291), 'ec': True, 'wait-over': True, 'desc': "2 left"},

            {'t': 'exchange_and_click', 'p': (470, 397), 'wait-over': True, 'desc': "2 lower left"},
            {'t': 'click', 'p': (820, 373), 'desc': "1 upper right"}
        ]
    },
    '25-2-sss-present-task': {
        'start': [
            ['swipe', (883, 347, 883, 189, 1)],
            ['shock1', (403, 675)],
            ['pierce1', (502, 235)],
        ],
        'action': [
            {'t': 'click', 'p': (677, 427), 'ec': True, 'desc': "1 upper right"},
            {'t': 'click', 'p': (693, 285), 'ec': True, 'wait-over': True, 'desc': "2 right"},

            {'t': 'click', 'p': (735, 418), 'ec': True, 'desc': "1 upper right"},
            {'t': 'choose_and_change', 'p': (735, 418), 'desc': "swap 1 2"},
            {'t': 'click', 'p': (850, 424), 'wait-over': True, 'ec': True, 'desc': "1 right"},

            {'t': 'exchange_and_click', 'p': (776, 305), 'ec': True, "desc": "2 upper left"},
            {'t': 'click', 'p': (585, 237), "wait-over": True, "desc": "1 upper right"},

            {'t': 'exchange_and_click', 'p': (716, 347), 'ec': True, "desc": "2 upper left"},
            {'t': 'choose_and_change', 'p': (636, 324), 'desc': "swap 1 2"},
            {'t': 'click', 'p': (750, 326), "wait-over": True, "desc": "1 right"},

            {'t': 'click', 'p': (812, 407), 'wait-over': True, 'desc': "2 lower right"},
            {'t': 'click', 'p': (574, 252), 'desc': "1 upper right"},
        ]
    },
    '25-3-sss-present-task': {
        'start': [
            ['shock1', (278, 382)],
            ['pierce1', (900, 648)],
            ['shock2', (963, 148)],
        ],
        'action': [
            {'t': 'click', 'p': (553, 305), 'ec': True, 'desc': "1 upper right"},
            {'t': 'click', 'p': (793, 401), 'ec': True, 'desc': "2 upper right"},
            {'t': 'click', 'p': (687, 389), 'ec': True, 'wait-over': True, 'desc': "3 lower left"},

            {'t': 'click', 'p': (616, 368), 'ec': True, 'desc': "1 right"},
            {'t': 'click', 'p': (800, 391), 'ec': True, 'desc': "2 upper right"},
            {'t': 'choose_and_change', 'p': (672, 501), 'desc': "swap 2 3"},
            {'t': 'click', 'p': (612, 588), 'ec': True, 'wait-over': True, 'desc': "3 lower left"},

            {'t': 'click', 'p': (377, 373), 'ec': True, 'desc': "1 left"},
            {'t': 'click', 'p': (725, 305), 'ec': True, 'desc': "2 upper left"},
            {'t': 'click', 'p': (564, 421), 'ec': True, 'wait-over': True, 'desc': "3 upper left"},

            {'t': 'click', 'p': (618, 357), 'ec': True, 'desc': "1 right"},
            {'t': 'click', 'p': (657, 345), 'ec': True, 'desc': "2 left"},
            {'t': 'click', 'p': (558, 424), 'ec': True, 'wait-over': True, 'desc': "3 upper left"},

            {'t': 'exchange_twice_and_click', 'p': (571, 392), 'ec': True, 'desc': "3 upper left"},
            {'t': 'exchange_and_click', 'p': (642, 324), 'desc': "2 left"},
            {'t': 'choose_and_change', 'p': (613, 406), 'desc': "swap 1 3"},
            {'t': 'choose_and_change', 'p': (675, 321), 'desc': "swap 1 2"},
            {'t': 'click', 'p': (615, 240), 'desc': "1 upper left"},
        ]
    },
}
