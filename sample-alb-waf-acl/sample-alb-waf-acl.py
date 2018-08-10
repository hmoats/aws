#!/usr/bin/python
#
# Get a sampled WAF results for a given WebAclId and RuleId for 
# definied time window (hours ago) from now (current time). You 
# must provide WebAclId and RuleId as arguments to get the sampled 
# results.
#
# hmoats
##################################################################

from pprint import pprint
import sys
import argparse
import boto3
import json
from botocore.exceptions import ClientError
from datetime import datetime, timedelta

# Parse args
parser = argparse.ArgumentParser(
    description = 'Get a sampled WAF results for a given WebAclId and RuleId for definied time window (hours ago) from now (current time). You must provide WebAclId and RuleId as arguments to get the sampled results')
parser.add_argument(
    '-region', 
    default = 'us-west-2',
    help = 'aws region (default: us-west-2)')
parser.add_argument(
    '-profile', 
    help = 'aws profile')
parser.add_argument(
    '-webaclid', 
    help = 'aws WAF WebAclId')
parser.add_argument(
    '-ruleid', 
    help = 'aws WAF WebAclId RuleId')
parser.add_argument(
    '-ago', 
    default = 60,
    help = 'minutes ago (default: 60, max 179)')
args = parser.parse_args()

# Required input profile
if not args.profile:
    print("argument profile is required\n")
    parser.print_help()
    exit()

# Required input webaclid
if not args.webaclid:
    print("argument webaclid is required\n")
    parser.print_help()
    exit()

# Required input ruleid
if not args.ruleid:
    print("argument ruleid is required\n")
    parser.print_help()
    exit()


##################################################################
# Serialize datetime for json output
def myConverter(o):
    if isinstance(o, datetime):
        return o.__str__()

##################################################################
# start boto3 session
session = boto3.Session(
    profile_name=args.profile
)

client = session.client(
    'waf-regional',
    region_name=args.region
)

try:
    response = client.get_sampled_requests(
        WebAclId = args.webaclid,
        RuleId = args.ruleid,
        TimeWindow = {
            'StartTime' : (datetime.utcnow() - timedelta(minutes = int(args.ago))).strftime("%Y-%m-%dT%H:%MZ"),
            'EndTime' : datetime.utcnow().strftime("%Y-%m-%dT%H:%MZ")
        },
        MaxItems = 500
    )
except ClientError as e:
    print json.dumps({"action" : e.response}, indent=4)
    sys.exit(1)

print json.dumps({"action" : response}, default = myConverter, indent=4)
