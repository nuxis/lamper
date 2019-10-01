#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import os
import sys


global colors
# 7 er taket, enkanals
# 8-9-10 er noen på pila, trekanals
# 11-12-13-14 er den siste på pila, firekanals
colors = {
    'off': {
        1: 0,
        # alle andre blir tomme (0)
    },
    'test': {
        1: 255,
        2: 255,
        3: 255,
        4: 255,
        5: 255,
        6: 255,
        7: 255,
        8: 255,
        9: 255,
        10: 255,
        11: 255,
        12: 255,
        13: 255,
        14: 255,
        15: 255,
        16: 255,
        17: 255,
        18: 255,
        19: 255,
        20: 255,
        21: 255,
        22: 255,
        23: 255,
    },
    'red': {
        1: 255,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 255,
        9: 0,

        '10': 255,
        '11': 255,
#        '12': 0,
#        '13': 0,
#        '14': 0,
#        '15': 0,
        '16': 0,
        '17': 0,
        '18': 255,
        '19': 0,
        '20': 0,
        '21': 0,
    },
    'green': {
        1: 0,
        2: 255,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 255,
        9: 0,
        
        '10': 255,
        '11': 255,
#        '12': 0,
#        '13': 0,
#        '14': 0,
#        '15': 0,
        '16': 0,
        '17': 0,
        '18': 0,
        '19': 255,
        '20': 0,
        '21': 0,
    },
    'yellow': {
        1: 255,
        2: 255,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 255,
        9: 0,
        
        '10': 255,
        '11': 255,
#        '12': 0,
#        '13': 0,
#        '14': 0,
#        '15': 0,
        '16': 0,
        '17': 0,
        '18': 0,
        '19': 255,
        '20': 255,
        '21': 0,
    },
}



global url
#url = ''
url = os.environ['LAMPER_URL']
global universe
universe = '1'


def web_post(url, payload):
    r = requests.post(
        url,
        data=payload,
        headers={'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
    )
    return r

def payload_creator(data):
    empty = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0,
        13: 0,
        14: 0,
        15: 0,
        16: 0,
        17: 0,
        18: 0,
        19: 0,
        20: 0,
        21: 0,
        22: 0,
    }

    payload = {**empty, **data}
    return ','.join(map(str, payload.values()))

def get_dmx():
    extra_url = url + '/get_dmx?u=' + universe
    print(web_post(extra_url, '').content)


def set_dmx(data):
    extra_url = url + '/set_dmx'
    payload = {
        'u': universe,
        'd': payload_creator(data),
    }

    import pprint
    pprint.pprint(payload)
    r = web_post(extra_url, payload)
    print(r.content)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('off, yellow, green or red?')
        sys.exit()

    if sys.argv[1] not in colors.keys():
        print('off, yellow, green or red?')
        sys.exit()
    color = sys.argv[1]


    set_dmx(colors[color])
    get_dmx()
