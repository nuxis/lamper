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
        i+1:0 for i in range(512)
    },
    'test': {
        i+1:255 for i in range(512)
    },
    'red': {
        1: 255,
        2: 255,
        3: 0,
        4: 0,
        5: 255,
        6: 0,
        7: 0,
        8: 0,
        9: 255,
        10: 0,
        11: 0,
        12: 0,
        
        13: 255,
        14: 255,
        15: 0,
        16: 0,
        17: 255,
        18: 0,
        19: 0,
        20: 0,
        21: 255,
        22: 0,
        23: 0,
        24: 0,
        
        25: 255,
        26: 255,
        27: 0,
        28: 0,
        29: 255,
        30: 0,
        31: 0,
        32: 0,
        33: 255,
        34: 0,
        35: 0,
        36: 0,
        
        37: 255,
        38: 255,
        39: 0,
        40: 0,
        41: 255,
        42: 0,
        43: 0,
        44: 0,
        45: 255,
        46: 0,
        47: 0,
        48: 0,
        
        49: 255,
        50: 255,
        51: 0,
        52: 0,
        53: 255,
        54: 0,
        55: 0,
        56: 0,
        57: 255,
        58: 0,
        59: 0,
        60: 0,
        
        61: 255,
        62: 255,
        63: 0,
        64: 0,
        65: 255,
        66: 0,
        67: 0,
        68: 0,
        69: 255,
        70: 0,
        71: 0,
        72: 0,
    },
    'green': {
        1: 255,
        2: 255,
        3: 255,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 255,
        11: 0,
        12: 0,
        
        13: 255,
        14: 255,
        15: 255,
        16: 0,
        17: 0,
        18: 0,
        19: 0,
        20: 0,
        21: 0,
        22: 255,
        23: 0,
        24: 0,
        
        25: 255,
        26: 255,
        27: 255,
        28: 0,
        29: 0,
        30: 0,
        31: 0,
        32: 0,
        33: 0,
        34: 255,
        35: 0,
        36: 0,
        
        37: 255,
        38: 255,
        39: 255,
        40: 0,
        41: 0,
        42: 0,
        43: 0,
        44: 0,
        45: 0,
        46: 255,
        47: 0,
        48: 0,
        
        49: 255,
        50: 255,
        51: 255,
        52: 0,
        53: 0,
        54: 0,
        55: 0,
        56: 0,
        57: 0,
        58: 255,
        59: 0,
        60: 0,
        
        61: 255,
        62: 255,
        63: 255,
        64: 0,
        65: 0,
        66: 0,
        67: 0,
        68: 0,
        69: 0,
        70: 255,
        71: 0,
        72: 0,
    },
    'yellow': {
        1: 255,
        2: 255,
        3: 128,
        4: 0,
        5: 128,
        6: 0,
        7: 0,
        8: 0,
        9: 255,
        10: 255,
        11: 0,
        12: 0,
        
        13: 255,
        14: 255,
        15: 128,
        16: 0,
        17: 128,
        18: 0,
        19: 0,
        20: 0,
        21: 255,
        22: 255,
        23: 0,
        24: 0,
        
        25: 255,
        26: 255,
        27: 128,
        28: 0,
        29: 128,
        30: 0,
        31: 0,
        32: 0,
        33: 255,
        34: 255,
        35: 0,
        36: 0,
        
        37: 255,
        38: 255,
        39: 128,
        40: 0,
        41: 128,
        42: 0,
        43: 0,
        44: 0,
        45: 255,
        46: 255,
        47: 0,
        48: 0,
        
        49: 255,
        50: 255,
        51: 128,
        52: 0,
        53: 128,
        54: 0,
        55: 0,
        56: 0,
        57: 255,
        58: 255,
        59: 0,
        60: 0,
        
        61: 255,
        62: 255,
        63: 128,
        64: 0,
        65: 128,
        66: 0,
        67: 0,
        68: 0,
        69: 255,
        70: 255,
        71: 0,
        72: 0,
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
