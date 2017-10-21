#!/usr/bin/env python3
import sys

PLDT_HEX_TABLE = {
    '0': 'f',
    '1': 'e',
    '2': 'd',
    '3': 'c',
    '4': 'b',
    '5': 'a',
    '6': '9',
    '7': '8',
    '8': '7',
    '9': '6',
    'a': '5',
    'b': '4',
    'c': '3',
    'd': '2',
    'e': '1',
    'f': '0',
}


def pldt_home_dsl(name):
    ssid = name.split('PLDTHOMEDSL')[1]
    pw = "PLDTHOMEDSL"
    pw += str(int(ssid) * 3)
    return pw


def pldt_home_fibr1(name):
    ssid = name.split('PLDTHOMEFIBR_')[1]
    pw = "wlan"

    for char in ssid:
        pw += PLDT_HEX_TABLE[char]
    return pw


def pldt_home_fibr2(name):
    ssid = name.split('PLDTHOMEFIBR')[1]
    pw = "PLDTWIFI"

    for char in ssid:
        pw += PLDT_HEX_TABLE[char]
    return pw


def main():
    name = sys.argv[1]
    print("name: ", name)
    if name.startswith('PLDTHOMEFIBR_'):
        pw = pldt_home_fibr1(name)
    elif name.startswith('PLDTHOMEFIBR'):
        pw = pldt_home_fibr2(name)
    if name.startswith('PLDTHOMEDSL'):
        pw = pldt_home_dsl(name)

    print("pass: ", pw)


if __name__ == '__main__':
    main()
