Description
============

The idea is to restrict ssh access to all my aws ec2 instances to my home or office network. The home/office public IP will change if we restart the router and hence it will always become an headache to update the new public ip with all the SG groups. It will be more difficult if we manage more accounts.

Solution
========
Written a python script to loop through profiles and sg groups and update the latest public IP of the home/office recursively in all the security groups.

Instructions
============

# Configure the ~/.aws/credentials file with all the profiles which we want to manage

# Install boto3 (python)

# Install requests (python)