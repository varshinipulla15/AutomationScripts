# Added pipeline for this file

import boto3
from botocore.exceptions import ClientError

def list_ec2_instances():
    ec2 = boto3.client('ec2')
    try:
        response = ec2.describe_instances()
        instances_list = []

        for reservation in response['Reservations']:
            for instance_details in reservation['Instances']:
                instance_id = instance_details['InstanceId']
                state = instance_details['State']['Name']
                instances_list.append((instance_id, state))
        return instances_list
    except ClientError as e:
        print (f'{e}')
        return []


def list_s3buckets():
    s3 = boto3.client('s3')
    try:
        response = s3.list_buckets()
        bucket_list = []

        for bucket_details in response['Buckets']:
            bucket_list.append(bucket_details['Name']) 
        return bucket_list
    except ClientError as e:
        print (f'{e}')
        return []


if __name__ == "__main__":
    ec2_instances = list_ec2_instances()
    if ec2_instances:
        for instance_id, state in ec2_instances:
            print (f'Ec2 id: {instance_id}, State: {state}')
    else:
        print ('No Ec2 Instances')

    s3_buckets = list_s3buckets()
    if s3_buckets:
        for bucket_name in s3_buckets:
            print (f'S3 Bucket: {bucket_name}')
    else:
        print ('No Buckets')
