# group-aws

Collection of aws scripts

```
group-aws/
├── list-aws-lb-ips
│   ├── list-aws-lb-ips.py
│   └── README.md
├── README.md
├── sample-alb-waf-acl
│   ├── README.md
│   └── sample-alb-waf-acl.py
└── update-alb-waf-acl
    ├── README.md
    └── update-alb-waf-acl.py
```

### list-aws-lb-ips

```
usage: list-aws-lb-ips.py [-h] [-region REGION] [-profile PROFILE]
                          [-output {raw,json}]

List all internet facing ELBs and ALBs public IPs.

optional arguments:
  -h, --help          show this help message and exit
  -region REGION      aws region (default: us-west-2)
  -profile PROFILE    aws profile
  -output {raw,json}  Output format (default: json)
```

### sample-alb-waf-acl
```
usage: sample-alb-waf-acl.py [-h] [-region REGION] [-profile PROFILE]
                             [-webaclid WEBACLID] [-ruleid RULEID] [-ago AGO]

Get a sampled WAF results for a given WebAclId and RuleId for definied time
window (hours ago) from now (current time). You must provide WebAclId and
RuleId as arguments to get the sampled results

optional arguments:
  -h, --help          show this help message and exit
  -region REGION      aws region (default: us-west-2)
  -profile PROFILE    aws profile
  -webaclid WEBACLID  aws WAF WebAclId
  -ruleid RULEID      aws WAF WebAclId RuleId
  -ago AGO            minutes ago (default: 60, max 179)
```

### update-alb-waf-acl
```
usage: update-alb-waf-acl.py [-h] [-region REGION] [-profile PROFILE]
                             [-arn ARN] [-webacl WEBACL]
                             [-action {add,remove,status}]

Program to add, remove, status aws WAF ACL for given ALB ARN.

optional arguments:
  -h, --help            show this help message and exit
  -region REGION        aws region (default: us-west-1)
  -profile PROFILE      aws profile
  -arn ARN              aws ALB ARN
  -webacl WEBACL        aws web ACL Id
  -action {add,remove,status}
                        {add,remove,status} for ALB ARN (default: status)
```
