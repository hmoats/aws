# update-alb-waf-acl

usage: update-alb-waf-acl.py [-h] [-region REGION] [-profile PROFILE]
                             [-arn ARN] [-webacl WEBACL]
                             [-action {add,remove,status}]

Program to add, remove, status aws WAF ACL for given ALB ARN.

optional arguments:
  -h, --help            show this help message and exit
  -region REGION        aws region (default: us-west-2)
  -profile PROFILE      aws profile
  -arn ARN              aws ALB ARN
  -webacl WEBACL        aws web ACL Id
  -action {add,remove,status}
                        {add,remove,status} for ALB ARN (default: status)
