Description
============

The idea is to restrict ssh access to all my aws ec2 instances to my home or office network. The home/office public IP will change if we restart the router and hence it will always become an headache to update the new public ip with all the SG groups. It will be more difficult if we manage more accounts.

Solution
========
Written a python script to loop through profiles and sg groups and update the latest public IP of the home/office recursively in all the security groups.

Prerequisite
============

- Shoudl have ~/.aws/credentials configured

- Should have python installed with the depended modules (boto3, os, requests etc)

- +x permission sould be given to the python script

- Settings option in the code should be udpated accordinlgy. (profiles, region, CidrDescription etc)

Instructions
============

Configure the ~/.aws/credentials file with all the profiles which we want to manage

Install boto3 (python)

Install requests (python)


--Settings--  | The following are hardcoded in the code now.  -- Will be updating soon

CidrDescription = "Subhash Home Network"

profiles = ['default','canon']

region = 'ap-southeast-1'