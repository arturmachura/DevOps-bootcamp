import boto3

ec2_client_frankfurt = boto3.client('ec2', region_name='us-west-1')
ec2_resource_frankfurt = boto3.resource('ec2', region_name='eu-central-1')

instances_ids_frankfurt = []

reservations_frankfurt = ec2_client_frankfurt.describe_instances()['Reservations']
for res in reservations_frankfurt:
    instances = res['Instances']
    for ins in instances:
        instances_ids_frankfurt.append(ins['InstanceId'])

response = ec2_resource_frankfurt.create_tags(
    Resources=instances_ids_frankfurt,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
    ]
)