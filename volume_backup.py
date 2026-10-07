import boto3
import schedule

ec2_client = boto3.client('ec2', region_name='eu-central-1')


def create_volume_snapshot():
    volumes = ec2_client.describe_volumes(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': ['production', 'staging']
            }
        ]
    )
    for volume in volumes['Volumes']:
        new_snapshot = ec2_client.create_snapshot(
            VolumeId=volume['VolumeId'],
        )


schedule.every(1).hours.do(create_volume_snapshot)

while True:
    schedule.run_pending()