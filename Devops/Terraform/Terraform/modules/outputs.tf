# S3 Module Outputs
output "s3_bucket_id" {
    description = "The ID of the S3 bucket"
    value       = module.s3_backend.s3_bucket_id
}

output "s3_bucket_arn" {
    description = "The ARN of the S3 bucket"
    value       = module.s3_backend.s3_bucket_arn
}

output "s3_bucket_name" {
    description = "The name of the S3 bucket"
    value       = module.s3_backend.s3_bucket_name
}

# EC2 Module Outputs
output "instance_id" {
    description = "The ID of the EC2 instance"
    value       = module.ec2_instance.instance_id
}

output "instance_public_ip" {
    description = "The public IP address of the EC2 instance"
    value       = module.ec2_instance.instance_public_ip
}

output "instance_private_ip" {
    description = "The private IP address of the EC2 instance"
    value       = module.ec2_instance.instance_private_ip
}

output "instance_arn" {
    description = "The ARN of the EC2 instance"
    value       = module.ec2_instance.instance_arn
}
