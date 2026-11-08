import boto3

ec2_client = boto3.client('ec2', region_name='us-west-2')
ec2_resources = boto3.resource('ec2', region_name='us-west-2')

instance_id = ""

volume = ec2_client.describe_volumes (
    Filters=[
        {
            'Name': '',
            'Values': []
        }
    ]
)

instance_volume = volumes[''][]
print(instance_volume)

ec2_client.describe_snapshots(
    OwnerIds=['self'],
    Filters = [
        {
            'Name': '',
            'Values': []
        }
    ]
)

Latest_snapshot = sorted(Snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)[0]
print(Latest_snapshot['StartTime'])

new_volume = ec2_client.create_volume(
    SnapshotID=latest_snapshot['SnapshotId'],
    AvailabilityZone='us-west-2a',
    TagSpecifications=[
        {
            'ResourceType': 'volume',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Restored Volume'
                }
            ]
        }
    ]

)

while True:
    ec_2_resources.Volume(new_volume[])
    print(vol.state)
    if vole.state == 'available':
        ec2_resources.Instance(instance_id).attach_volume(
            VolumeId=new_volume['VolumeId'],
            Device='dev/xvdb'
)
