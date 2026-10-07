import boto3

ec2_client = boto3.client('ec2', region_name='us-west-1')
ec2_resource = boto3.resource('ec2', region_name='us-west-1')

reservations = ec2_resource.instances.all()
for reservation in reservations['Reservations']:
    instances = reservation['Instances']
    for instance in instances:
        print(f"Status of instance: {instance['InstanceId']}: {instance['State']}")

statuses = ec2_client.describe_instances_status()
for status in statuses['InstanceStatuses']:
    ins_status = status['InstanceState']['Status']
    sys_status = status['SystemStatus']['Status']
    state = status['InstanceState']['Name']
    print(f"{status['InstanceId']} is {state} - Instance Status: {ins_status}, System Status: {sys_status}")
