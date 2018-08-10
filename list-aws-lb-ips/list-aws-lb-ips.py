#!/usr/bin/python
#
# List all internet facing ELBs and ALBs public IPs.
#
# hmoats
##################################################################

from pprint import pprint
from socket import inet_aton
import argparse
import boto3
import socket
import struct
import json

# parse args
parser = argparse.ArgumentParser(
    description = 'List all internet facing ELBs and ALBs public IPs.')
parser.add_argument(
    '-region', 
    default = 'us-west-2',
    help = 'aws region (default: us-west-2)')
parser.add_argument(
    '-profile', 
    help='aws profile')
parser.add_argument(
    '-output', 
    default='json',
    choices=['raw','json'],
    help='Output format (default: json)')
args = parser.parse_args()

# we need at least arg region and profile
if not args.profile:
    print('require argument profile missing')
    parser.print_help()
    exit()

# start boto3 session
session = boto3.Session(
    profile_name = args.profile
)

# start address list
addresses = [];
addressesdict = {};

# elbs 
elb_client = session.client(
    'elb',
    region_name=args.region
)

elb_response = elb_client.describe_load_balancers();
for elb in elb_response['LoadBalancerDescriptions']:
    if elb['Scheme'] == 'internet-facing':
        try:
            addr = socket.gethostbyname_ex(elb['DNSName'])
        except socket.error, msg:
            print "Error: %s %s" % (socket.error, msg)
        #print(addr[0], addr[2])
        addressesdict[addr[0]] = addr[2]
        addresses.extend(addr[2])

# albs
alb_client = session.client(
    'elbv2',
    region_name=args.region
)
alb_response = alb_client.describe_load_balancers();
for alb in alb_response['LoadBalancers']:
    if alb['Scheme'] == 'internet-facing':
        try:
            addr = socket.gethostbyname_ex(alb['DNSName'])
        except socket.error, msg:
            print("Error: %s %s" % (socket.error, msg))
        #print(addr[0], addr[2])
        addressesdict[addr[0]] = addr[2]
        addresses.extend(addr[2])

# sort addresses
addresses = sorted(addresses, key=lambda ip: struct.unpack("!L", inet_aton(ip))[0])

# output
if args.output == 'raw':
    for ip in addresses:
        print(format(ip))
else:
    print json.dumps({"LBs" : addressesdict}, indent=4)
