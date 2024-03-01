stage_data = {
    '19': {
        'SUB': "pierce1"
    },
    '19-1': {
        'start': [
            ['pierce1', (377, 391)],
            ['mystic1', (741, 561)],
        ],
        'action': [
            {'t': 'click', 'p': (628, 338), 'ec': True, "desc": "1 right"},
            {'t': 'click', 'p': (841, 484), "wait-over": True, "desc": "2 right"},

            {'t': 'click', 'p': (607, 222), 'ec': True, "desc": "1 upper right"},
            {'t': 'click', 'p': (799, 385), "wait-over": True, "desc": "2 upper right"},

            {'t': 'exchange_and_click', 'ec': True,'p': (872, 466), "desc": "2 right"},
            {'t': 'click', 'p': (641, 321), "desc": "1 right"},
        ]
    },
    '19-2': {
        'start': [
            ['pierce1', (547, 555)],
            ['mystic1', (537, 391)],
        ],
        'action': [
            {'t': 'click', 'p': (753, 383), 'ec': True, "desc": "1 upper right"},
            {'t': 'click', 'p': (582, 311), 'ec': True, "wait-over": True, "desc": "2 upper left"},

            {'t': 'click', 'p': (570, 353), 'ec': True, "desc": "1 upper right"},
            {'t': 'click', 'p': (442, 287), 'ec': True, "wait-over": True, "desc": "2 upper left"},

            {'t': 'exchange_and_click', 'p': (628, 350), 'ec': True, "desc": "2 right"},
            {'t': 'click', 'p': (841, 339), 'wait-over': True, "desc": "1 upper right"},

            {'t': 'exchange_and_click', 'p': (485, 269), 'ec': True, "desc": "2 upper left"},
            {'t': 'click', 'p': (842, 309), "desc": "1 upper right"},
        ]
    },
    '19-3': {
        'start': [
            ['pierce1', (461, 556)],
            ['mystic1', (445, 141)],
        ],
        'action': [
            {'t': 'click', 'p': (717, 416), 'ec': True, "desc": "1 upper right"},
            {'t': 'click', 'p': (707, 275), 'ec': True, "desc": "2 right"},

            {'t': 'click', 'p': (782, 400), 'ec': True, "desc": "1 upper right"},
            {'t': 'click', 'p': (716, 353), 'ec': True, "desc": "2 lower right"},

            {'t': 'exchange_and_click', 'p': (841, 357), 'ec': True, "desc": "2 right"},
            {'t': 'choose_and_change', 'p': (784, 364), "desc": "swap 1 2"},
            {'t': 'click', 'p': (906, 367), 'wait-over': True, "desc": "1 right"},

            {'t': 'exchange_and_click', 'p': (559, 449), 'ec': True, "desc": "2 lower right"},
            {'t': 'click', 'p': (732, 199), "wait-over": True, "desc": "1 upper right"},

            {'t': 'click', 'p': (809, 290), "desc": "1 right"},
        ]
    },
    '19-4': {
        'start': [
            ['pierce1', (376, 342)],
            ['mystic1', (800, 453)],
        ],
        'action': [
            {'t': 'click', 'p': (619, 360), 'ec': True, "desc": "1 right"},
            {'t': 'click', 'p': (652, 439), 'wait-over': True, 'ec':True,"desc": "2 left"},

            {'t': 'exchange'},
            {'t': 'choose_and_change', 'p': (523, 318), "desc": "swap 1 2"},
            {'t': 'click', 'p': (643, 318), 'ec': True, "desc": "2 right"},
            {'t': 'click', 'p': (653, 311), 'wait-over': True, "desc": "1 right"},

            {'t': 'click', 'p': (695, 450), 'ec': True, "desc": "1 lower right"},
            {'t': 'click', 'p': (517, 203), 'wait-over': True, "desc": "2 upper left"},

            {'t': 'exchange_and_click', 'p': (625, 213), 'ec': True, "desc": "2 upper right"},
            {'t': 'click', 'p': (661, 459), "wait-over": True, "desc": "1 lower left"},


            {'t': 'exchange_and_click', 'p': (749, 275), 'ec': True, "desc": "2 right"},
            {'t': 'click', 'p': (539, 516), "desc": "1 left"},
        ]
    },
    '19-5': {
        'start': [
            ['pierce1', (319, 384)],
            ['mystic1', (862, 561)],
        ],
        'action': [
            {'t': 'click', 'p': (623, 342), 'ec': True, "desc": "1 right"},
            {'t': 'click', 'p': (700, 375), 'wait-over': True, "desc": "2 upper left"},

            {'t': 'click', 'p': (709, 447), 'ec': True, "desc": "1 right"},
            {'t': 'choose_and_change', 'p': (670, 398), "desc": "swap 1 2"},
            {'t': 'click', 'p': (725, 314), 'wait-over': True, "desc": "2 upper right"},

            {'t': 'click', 'p': (787, 405), 'ec': True, "desc": "1 upper right"},
            {'t': 'click', 'p': (782, 236), 'ec': True, "desc": "2 upper right"},

            {'t': 'exchange_and_click', 'p': (844, 300), 'ec': True, "desc": "2 right"},
            {'t': 'click', 'p': (721, 444), "wait-over": True, "desc": "1 right"},

            {'t': 'exchange_and_click', 'p': (703, 410), 'ec': True, "desc": "2 lower right"},
            {'t': 'click', 'p': (761, 490), "desc": "1 right"},
        ]
    },
}
