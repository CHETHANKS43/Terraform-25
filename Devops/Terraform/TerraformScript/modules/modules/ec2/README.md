# EC2 Instance Module

This module creates an EC2 instance with configurable AMI, instance type, key pair, and instance name.

## Resources Created

- `aws_instance` - The EC2 instance

## Variables

- `ami_id` (string, default: "ami-0f918f7e67a3323f0") - The AMI ID to use for the EC2 instance
- `instance_type` (string, default: "t2.micro") - The type of EC2 instance to launch
- `key_name` (string, required) - The name of the key pair to use for the EC2 instance
- `instance_name` (string, default: "TestEC2Instance") - The name tag for the EC2 instance

## Outputs

- `instance_id` - The ID of the EC2 instance
- `instance_public_ip` - The public IP address of the EC2 instance
- `instance_private_ip` - The private IP address of the EC2 instance
- `instance_arn` - The ARN of the EC2 instance

## Usage

```hcl
module "ec2_instance" {
    source        = "./modules/ec2"
    ami_id        = "ami-0f918f7e67a3323f0"
    instance_type = "t2.micro"
    key_name      = "my-key-pair"
    instance_name = "MyEC2Instance"
}
```
