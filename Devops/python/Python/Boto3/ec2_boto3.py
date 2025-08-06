import boto3
from dotenv import load_dotenv
import os

load_dotenv()
aws_session = boto3.Session(
    region_name=os.getenv('AWS_REGION_ID'),
    aws_access_key_id=os.getenv('AWS_EC2_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_EC2_SECRET_ACCESS_KEY')
)

ec2_client = aws_session.client('ec2')
ec2_resource = aws_session.resource('ec2')

def create_ec2_instance(key_name, instance_type='t2.micro', ami_id='ami-0522ab6e1ddcc7055'):
    """Create a single EC2 instance with tags"""
    try:
        response = ec2_client.run_instances(
            ImageId=ami_id,
            InstanceType=instance_type,
            KeyName=key_name,
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[{
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': "boto3_tutorial"}]
            }]
        )
        instance_id = response['Instances'][0]['InstanceId']
        print(f"Instance created: {instance_id}")
        return instance_id
    except Exception as e:
        print(f"Error creating instance: {e}")
        return None

def create_ec2_fleet(launch_template_id, target_capacity):
    """Create an EC2 fleet using launch templates"""
    try:
        response = ec2_client.create_fleet(
            LaunchTemplateConfigs=[{
                'LaunchTemplateSpecification': {
                    'LaunchTemplateId': launch_template_id,
                    'Version': '$Latest'
                }
            }],
            TargetCapacitySpecification={
                'TotalTargetCapacity': target_capacity,
                'DefaultTargetCapacityType': 'on-demand'
            }
        )
        print(f"Fleet created: {response['FleetId']}")
        return response['FleetId']
    except Exception as e:
        print(f"Error creating fleet: {e}")
        return None

def search_instances(filters=None):
    """Search instances by type, name, security group, etc."""
    try:
        if not filters:
            filters = []
            
        response = ec2_client.describe_instances(Filters=filters)
        instances = []
        
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instances.append({
                    'InstanceId': instance['InstanceId'],
                    'InstanceType': instance['InstanceType'],
                    'State': instance['State']['Name'],
                    'Tags': instance.get('Tags', []),
                    'SecurityGroups': instance.get('SecurityGroups', [])
                })
        return instances
    except Exception as e:
        print(f"Error searching instances: {e}")
        return []

def list_ec2_instances(return_ids=False, filters=None):
    """List all instances with optional filtering"""
    try:
        instances = search_instances(filters)
        
        if return_ids:
            return [i['InstanceId'] for i in instances]
            
        for instance in instances:
            name = next((tag['Value'] for tag in instance['Tags'] if tag['Key'] == 'Name'), 'N/A')
            print(f"\nInstance ID: {instance['InstanceId']}")
            print(f"Name: {name}")
            print(f"Type: {instance['InstanceType']}")
            print(f"State: {instance['State']}")
            print(f"Security Groups: {[sg['GroupName'] for sg in instance['SecurityGroups']]}")
    except Exception as e:
        print(f"Error listing instances: {e}")
        return [] if return_ids else None

def stop_ec2_instances(instance_ids):
    """Stop one or more instances"""
    try:
        response = ec2_client.stop_instances(InstanceIds=instance_ids)
        print(f"Stopping instances: {instance_ids}")
        return response
    except Exception as e:
        print(f"Error stopping instances: {e}")
        return None

def terminate_ec2_instances(instance_ids=None):
    """Terminate instances (all if no IDs provided)"""
    try:
        if not instance_ids:
            instance_ids = list_ec2_instances(return_ids=True)
            if not instance_ids:
                print("No instances to terminate")
                return None
                
        response = ec2_client.terminate_instances(InstanceIds=instance_ids)
        print(f"Terminating instances: {instance_ids}")
        return response
    except Exception as e:
        print(f"Error terminating instances: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    print("=== Creating Single Instance ===")
    new_instance = create_ec2_instance('boto3')
    
    print("\n=== Listing All Instances ===")
    list_ec2_instances()
    
    print("\n=== Searching Instances by Type ===")
    t2_instances = search_instances([{'Name': 'instance-type', 'Values': ['t2.micro']}])
    print(f"Found {len(t2_instances)} t2.micro instances")
    
    print("\n=== Searching Instances by Name ===")
    named_instances = search_instances([{'Name': 'tag:Name', 'Values': ['boto3_tutorial']}])
    print(f"Found {len(named_instances)} named instances")
    
    print("\n=== Stopping Instance ===")
    if new_instance:
        stop_ec2_instances([new_instance])
    
    print("\n=== Terminating All Instances ===")
    terminate_ec2_instances()