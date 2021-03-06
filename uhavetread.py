#!/usr/bin/python
#
# Copyright (c) 2019 mttaat <mttaat@protonmail.com>. All Rights Reserved.
# This file licensed under the GPLv3
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# uhavetread v0.1
# simple domain resolver and subdomain brute forcer
#
# # # # # # # # 
#
# @mttaat
# https://mttaat.net
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import sys
import socket
#import argparse
import string

def usage():
    print("USAGE:   python uhavetread.py -d <root domain> -s </path/to/subdomains.txt> (-1)")
    print("or:      python uhavetread.py -d <root domain> -s <'subdmain,subdomain,subdomain'>")

def subslist():
    subs = []
    # TODO: make string methods py3 compatible
    subslist = str(sys.argv[sys.argv.index('-s') + 1])
    if string.find(subslist, ',') == -1:
        f = open(subslist, 'r')
        for line in f:
            if string.find(line, '#') != 0:
                subs.append(string.strip(line))
    else:
        subs = subslist.split(',')
    return subs

def loopbody():
    rootdomain = str(sys.argv[sys.argv.index('-d') + 1])
    subs = subslist()
    # TODO: refactor with list comprehensions and multithreading
    for sub in subs:
        targetdomain = sub + '.' + rootdomain
        try:
            result = socket.gethostbyname_ex(targetdomain)
            if(sys.argv.count('-1') > 0):
                print(targetdomain + ' = hostname: ' + str(result[0]) + ' / aliases: ' + str(result[1]) + ' / IPs: ' + str(result[2]) + '\n')
            else:
                print(targetdomain)
                print('  + hostname:    ' + str(result[0]))
                print('  + aliases:     ' + str(result[1][0]))
                if(len(result[1]) > 1):
                    for i in result[1]:
                        print('                 ' + str(i))
                print('  + IPs:         ' + str(result[2][0]))
                if(len(result[2]) > 1):
                    for i in result[2]:
                        print('                 ' + str(i))       
                print('--------')
            continue
        except(OSError, socket.gaierror):
            print(targetdomain + ' - unable to resolve')
            print('--------')
            continue

if len(sys.argv) < 2:
    usage()
    sys.exit()

loopbody()
