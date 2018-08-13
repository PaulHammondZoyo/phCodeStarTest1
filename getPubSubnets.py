import json
import boto3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--vpcid",
                    help="echo the vpc you use here",
                    required=True)
args = parser.parse_args()

print (args.vpcid)

ec2client = boto3.client('ec2')

response = ec2client.describe_subnets(
    Filters=[
        {
            'Name': 'tag:Role',
            'Values': [
                'private',
            ]
        },
    ]
)

subnets = []
for subnet in response['Subnets']:
    print("here")
    print(subnet['AvailabilityZone'], subnet['SubnetId'])
    subnets.append(subnet['SubnetId'])

#
print("Full List: %s" % (":".join(subnets)))