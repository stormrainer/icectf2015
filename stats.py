#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        stats.py
# Purpose:     icec 2015 challenge
#
# Author:      StormRainer
#
# Created:     12/08/2015
# Copyright:   (c) StormRainer 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import socket
import sys

HOST        = 'vuln2015.icec.tf'
BUFFER_SIZE = 4096
TCP_PORT    = 9000

def getData(s):
    data = s.recv(BUFFER_SIZE)
    #print data
    #if not data: break
    count = 0
    print data
    dataList = data.split("\n")
    for word in dataList:
        print word
        templist = word.split(" ")
        for temp in templist:
            if temp.isdigit():
                count =+ int(temp)
                print count
        if count > 0: print count

def main():
    try:
        #creat a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
        print 'Failed to create socket. Error code: " + str(msg[0]) + " , Error message : ' + msg[1]
        sys.exit();
    pass

    print "socket created"

    try:
        remote_ip = socket.gethostbyname(HOST)
    except socket.gaierror:
        #could not resolve host
        print 'Hostname could not be resolve. Exiting'
        sys.exit()
    print 'Ip address of ' + HOST + ' is ' + remote_ip

    s.connect((remote_ip, TCP_PORT))
    print 'Socket connected to ' + HOST + ' on ip ' + remote_ip

    getData(s)
    s.send('6915\n')
    getData(s)
    s.send('27\n')
    getData(s)
    s.send('9802\n')
    getData(s)
    s.send('1873\n')
    getData(s)
    s.send('336\n')
    getData(s)
    s.send('291411\n')
    getData(s)
    s.send('723')
    getData(s)
    s.send('2350')
    #getData(s)
    #s.shutdown()
    s.close()
    print "socket destroyed"


if __name__ == '__main__':
    main()

#strings to search for minimum, maximum, average
# make list based on space
#search for keywords in second line
