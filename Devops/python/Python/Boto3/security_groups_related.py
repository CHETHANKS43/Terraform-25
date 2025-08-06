import boto3

# Define the AWS region
region = 'your-region'

# Initialize EC2 client
ec2_client = boto3.client('ec2', region_name=region)


# Function to create a security group with specified inbound rules
def create_security_group(group_name, description, vpc_id):
    try:
        response = ec2_client.create_security_group(
            GroupName=group_name,
            Description=description,
            VpcId=vpc_id
        )
        security_group_id = response['GroupId']
        print("Security group created with ID:", security_group_id)

        # Add inbound rules to allow traffic on ports 80, 443, and 3606
        ec2_client.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 80,
                    'ToPort': 80,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                },
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 443,
                    'ToPort': 443,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                },
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 3606,
                    'ToPort': 3606,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                }
            ]
        )

        print("Inbound rules added to allow traffic on ports 80, 443, and 3606")

        return security_group_id
    except Exception as e:
        print("Error creating security group:", str(e))


# Main function
def main():
    # Create a security group
    security_group_id = create_security_group('MySecurityGroup', 'My security group description', 'vpc-123456')


if __name__ == "__main__":
    main()
