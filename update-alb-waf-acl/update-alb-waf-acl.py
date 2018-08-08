#!/usr/bin/python
#
# Program to add, remove or status aws WAF ACL for given ALB ARN.
# Output is json.
#
##################################################################
from pprint import pprint
import sys
import argparse
import boto3
import json
from botocore.exceptions import ClientError

# Parse args
parser = argparse.ArgumentParser(
    description = 'Program to add, remove, status aws WAF ACL for given ALB ARN.')
parser.add_argument(
    '-region', 
    default = 'us-west-1',
    help = 'aws region (default: us-west-1)')
parser.add_argument(
    '-profile', 
    help = 'aws profile')
parser.add_argument(
    '-arn', 
    help = 'aws ALB ARN')
parser.add_argument(
    '-webacl', 
    help = 'aws web ACL Id')
parser.add_argument(
    '-action', 
    default = 'status',
    choices = ['add','remove','status'],
    help = '{add,remove,status} for ALB ARN (default: status)')
args = parser.parse_args()

# Required input profile
if not args.profile:
    parser.print_help()
    exit()

# If action is add we need web ACL ID
if args.action == 'add' and not args.webacl:
    parser.print_help()
    exit()

##################################################################
# start boto3 session
session = boto3.Session(
    profile_name=args.profile
)

client = session.client(
    'waf-regional',
    region_name=args.region
)

##################################################################
# Check for ALB ARN
def checkResource(profile, action, arn): 
    try:
        response = client.get_web_acl_for_resource(
            ResourceArn=args.arn
       )
    except ClientError as e:
        print json.dumps({"action" : {action : e.response, "result" : False}, "arn" : arn, "profile" : profile}, indent=4)
        sys.exit(1)
    
    if "WebACLSummary" in response:
        print json.dumps({"action" : {action : response, "result" : True, "arn" : arn, "profile" : profile}}, indent=4)
    else:
        response["WebACLSummary"] = {"Message" : "No WebACLSummary for ARN", "Code" : "NoWebACLSummary"}
        print json.dumps({"action" : {action : response, "result" : False, "arn" : arn, "profile" : profile}}, indent=4)
    return;

##################################################################
# Main
if args.action == 'remove':
    try:
        response = client.disassociate_web_acl(
            ResourceArn=args.arn
        )
    except ClientError as e:
        print json.dumps({"action" : {args.action : e.response, "result" : False, "arn" : args.arn, "profile" : args.profile}}, indent=4)
        sys.exit(1)
    checkResource(args.profile, args.action, args.arn)
elif args.action == 'add':
    try:
        response = client.associate_web_acl(
            ResourceArn=args.arn,
            WebACLId=args.webacl
        )
    except ClientError as e:
        print json.dumps({"action" : {args.action : e.response, "result" : False, "arn" : args.arn, "profile" : args.profile}}, indent=4)
        sys.exit(1)
    checkResource(args.profile, args.action, args.arn)
else:
    checkResource(args.profile, args.action, args.arn)
