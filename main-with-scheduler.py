import boto3
import schedule

ec2_client = boto3.client('ec2', region_name='us-west-1')
ec2_resource = boto3.resource('ec2', region_name='us-west-1')

def check_instance_status():
    statuses = ec2_client.describe_instances_status()
    for status in statuses['InstanceStatuses']:
        ins_status = status['InstanceState']['Status']
        sys_status = status['SystemStatus']['Status']
        state = status['InstanceState']['Name']
        print(f"{status['InstanceId']} is {state} - Instance Status: {ins_status}, System Status: {sys_status}")

schedule.every(10).seconds.do(check_instance_status)

while True:
    schedule.run_pending()
    time.sleep(1)