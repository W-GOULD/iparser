#! /usr/bin/python3

import sys
import os
import  xml.etree.ElementTree as ET
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument("-i",dest="input_file", required=True, help="Input file: This is the file you want to parses for information.")
    parser.add_argument("--linux", dest="linux_hosts", action="store_true", required=False, help="This flag will find linux hosts and will parses the IP addresses in to another file")
    parser.add_argument("--windows", dest="windows_hosts", action="store_true", required=False, help="This will find Windows hosts from the input file.")
    parser.add_argument("--mail", dest="mail_servers", action="store_true", required=False, help="This will find mail servers from the input file.")
    parser.add_argument("--ips", dest="ip_finder", action="store_true", required=False, help="Grab ips from the input file.")
    parser.add_argument("-t", dest="test", action="store_true", required=False, help=" ")

    arguments = parser.parse_args()
    input_file = arguments.input_file
    linux = arguments.linux_hosts
    windows = arguments.windows_hosts
    mail = arguments.mail_servers
    ip_find = arguments.ip_finder

    if len(sys.argv) == 0:
        print("Were them arguments man?!")

    if input_file is False:
        print("Please specify a file you would like to parse")

    else:
        _t = ET.parse(input_file)
        _r = _t.getroot()

    if ip_find is True:
        for address in _r.iter('address'):
            print (address.attrib['addr'])

    if arguments.test is True:
        for host in _r:
            for port in _r.iter('port'):
                print (port.attrib['portid'])


if __name__ == "__main__":
    main()