stage_data = {
    '22': {
        'SUB': "pierce1"
    },
    '22-1': {
        'start': [
            ['pierce1', (823, 515)],
            ['mystic1', (382, 290)],
        ],
        'action': [
            {'t': 'click_and_teleport', 'p': (700, 539), 'ec': True, "desc": "1 lower left and tp"},
            {'t': 'click', 'p': (644, 317), "wait-over": True, 'ec': True, "desc": "2 right"},

            {'t': 'click', 'p': (526, 484), 'ec': True, "desc": "1 left"},
            {'t': 'click', 'p': (773, 308), "wait-over": True, 'ec': True, "desc": "2 right"},

            {'t': 'click', 'p': (500, 230), 'ec': True, "desc": "1 upper left"},
            {'t': 'click', 'p': (840, 296), "wait-over": True, 'ec': True, "desc": "2 upper right"},

            {'t': 'click', 'p': (440, 290), "desc": "1 upper left"},
        ]
    },
    '22-2': {
        'start': [
            ['pierce1', (493, 261)],
            ['mystic1', (887, 463)],
        ],
        'action': [
            {'t': 'click', 'p': (580, 402), 'ec': True, "desc": "1 lower right"},
            {'t': 'click', 'p': (650, 446), 'ec': True, "wait-over": True, "desc": "2 left"},

            {'t': 'exchange_and_click', 'p': (614, 365), 'ec': True, "desc": "2 upper left"},
            {'t': 'choose_and_change', 'p': (614, 359), "desc": "swap 1 2"},
            {'t': 'click', 'p': (673, 444), "wait-over": True, "desc": "1 lower right"},

            {'t': 'click', 'p': (617, 535), 'ec': True, "desc": "1 lower left"},
            {'t': 'click', 'p': (446, 420), 'ec': True, "wait-over": True, "desc": "2 lower left"},

            {'t': 'exchange_and_click', 'p': (385, 347), 'ec': True, "desc": "2 left"},
            {'t': 'click', 'p': (691, 451), "desc": "1 lower left"},
        ]
    },
    '22-3': {
        'start': [
            ['pierce1', (908, 303)],
            ['mystic1', (481, 605)],
        ],
        'action': [
            {'t': 'click', 'p': (697, 396), 'ec': True, "desc": "1 lower left"},
            {'t': 'click', 'p': (605, 394), 'ec': True, "desc": "2 upper right"},

            {'t': 'exchange_and_click', 'p': (644, 322), 'ec': True, "desc": "2 upper left"},
            {'t': 'choose_and_change', 'p': (644, 322), "desc": "swap 1 2"},
            {'t': 'click', 'p': (580, 236), "wait-over": True, "desc": "1 upper right"},

            {'t': 'click', 'p': (536, 197), 'ec': True, "desc": "1 upper left"},
            {'t': 'click', 'p': (650, 437), 'ec': True, "desc": "2 left"},

            {'t': 'click', 'p': (442, 290), 'ec': True, "desc": "1 left"},
            {'t': 'click', 'p': (610, 487), "wait-over": True, 'ec': True, "desc": "2 left"},

            {'t': 'exchange_and_click', 'p': (596, 485), 'ec': True, "desc": "2 left"},
            {'t': 'click', 'p': (550, 254), "desc": "1 upper right"},
        ]
    },
    '22-4': {
        'start': [
            ['pierce1', (494, 387)],
            ['mystic1', (928, 144)],
        ],
        'action': [
            {'t': 'click_and_teleport', 'p': (458, 539), 'ec': True, "desc": "1 lower left and tp"},
            {'t': 'click_and_teleport', 'p': (614, 300), 'ec': True, "wait-over": True, "desc": "2 left and tp"},

            {'t': 'exchange_and_click', 'p': (550, 360), 'ec': True, "desc": "2 lower left"},
            {'t': 'click', 'p': (715, 428), "wait-over": True, "desc": "1 upper right"},

            {'t': 'click', 'p': (610, 338), 'ec': True, "desc": "1 upper left"},
            {'t': 'choose_and_change', 'p': (628, 338), "desc": "swap 1 2"},
            {'t': 'click', 'p': (683, 263), "wait-over": True, "ec": True, "desc": "2 upper right"},

            {'t': 'click', 'p': (441, 274), 'ec': True, "desc": "1 upper left"},
            {'t': 'click', 'p': (876, 321), "wait-over": True, 'ec': True, "desc": "2 right"},

            {'t': 'exchange_and_click', 'p': (906, 378), 'ec': True, "desc": "2 right"},
            {'t': 'click', 'p': (497, 357), "desc": "1 left"},

        ]
    },
    '22-5': {
        'start': [
            ['pierce1', (340, 387)],
            ['mystic1', (919, 468)],
        ],
        'action': [
            {'t': 'exchange_and_click', 'p': (724, 339), 'ec': True, "desc": "2 upper left"},
            {'t': 'click', 'p': (557, 278), "wait-over": True, "desc": "1 upper right"},


            {'t': 'click', 'p': (769, 312), 'ec': True, "desc": "1 right"},
            {'t': 'click', 'p': (666, 395), "wait-over": True, 'ec': True, "desc": "2 left"},

            {'t': 'choose_and_change', 'p': (666, 359), "desc": "swap 1 2"},
            {'t': 'click', 'p': (782, 360), "wait-over": True, "desc": "1 right"},
            {'t': 'click', 'p': (548, 194), "wait-over": True, "desc": "2 upper left"},

            {'t': 'click', 'p': (900, 400), 'ec': True, "desc": "1 right"},
            {'t': 'click', 'p': (590, 228), "wait-over": True, 'ec': True, "desc": "2 upper right"},

            {'t': 'exchange_and_click', 'p': (611, 215), 'ec': True, "desc": "2 upper right"},
            {'t': 'click', 'p': (746, 422), "desc": "2 right"},
        ]
    },
}
