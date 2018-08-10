# sample-alb-waf-acl
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
