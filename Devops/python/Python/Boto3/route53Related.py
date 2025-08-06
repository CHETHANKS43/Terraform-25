import boto3
from dotenv import load_dotenv
import os

load_dotenv()
aws_session = boto3.Session(
    region_name=os.getenv('AWS_REGION_ID'),
    aws_access_key_id=os.getenv('AWS_EC2_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_EC2_SECRET_ACCESS_KEY')
)
route53_client = aws_session.client('route53')


# Function to create a hosted zone
def create_hosted_zone(domain_name):
    try:
        response = route53_client.create_hosted_zone(
            Name=domain_name,
            CallerReference=str(hash(domain_name))
        )
        hosted_zone_id = response['HostedZone']['Id']
        print("Hosted zone created with ID:", hosted_zone_id)
        return hosted_zone_id
    except Exception as e:
        print("Error creating hosted zone:", str(e))


# Function to create a record set in a hosted zone
def create_record_set(hosted_zone_id, record_name, record_type, record_value):
    try:
        response = route53_client.change_resource_record_sets(
            HostedZoneId=hosted_zone_id,
            ChangeBatch={
                'Changes': [
                    {
                        'Action': 'UPSERT',
                        'ResourceRecordSet': {
                            'Name': record_name,
                            'Type': record_type,
                            'TTL': 300,
                            'ResourceRecords': [
                                {
                                    'Value': record_value
                                },
                            ]
                        }
                    },
                ]
            }
        )
        print("Record set created successfully.")
    except Exception as e:
        print("Error creating record set:", str(e))


# Main function
def main():
    # Create a hosted zone
    hosted_zone_id = create_hosted_zone('itdefined.com')

    # Add a record set to the hosted zone
    create_record_set(hosted_zone_id, 'itdefined.com', 'A', '1.2.3.4')


if __name__ == "__main__":
    main()
