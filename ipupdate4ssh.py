#!/usr/bin/env python
import boto3
from botocore.exceptions import ClientError
import requests
import os

#Settings
CidrDescription = "Subhash Home Network"
profiles = ['default','myprofile1']
region = 'ap-southeast-1'

myList = []

for profile in profiles:
	os.environ["AWS_PROFILE"]=profile
	os.environ["AWS_DEFAULT_REGION"] = region

	MyPublicIp=(requests.get('http://v4.ifconfig.co/ip')).text
	MyPublicIp=MyPublicIp.strip()+'/32'
	
	print "PROFILE >>>>"+profile

	session = boto3.Session(profile_name=profile)
	ec2 = session.resource('ec2')

	# ec2 = boto3.resource('ec2')

	for instance in ec2.instances.all():
		security_group = ec2.SecurityGroup(instance.id)
		for sg in instance.security_groups:
			# print "Setting Rules for Security GroupId "+str(sg['GroupId'])
			if str(sg['GroupId']) not in myList: # to make sure that same sg group executes more than once
				myList.insert(len(myList)-1,str(sg['GroupId']))
				try:
					response = security_group.authorize_ingress(
					    GroupId=str(sg['GroupId']),
					    IpPermissions=[
					        {
					            'FromPort': 22,
					            'IpProtocol': 'tcp',
					            'IpRanges': [
					                {
					                    'CidrIp': MyPublicIp,
					                    'Description': CidrDescription
					                },
					            ],
					            'ToPort': 22,
					        },
					    ],
					    DryRun=False
					)

					print "Success : "+str(response)
				except ClientError as e: print(e)

	print myList


