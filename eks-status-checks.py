import boto3
import schedule

client = boto3.client('eks', region_name='us-west-1')