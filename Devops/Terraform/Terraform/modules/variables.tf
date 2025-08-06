# The name of the S3 bucket to be used as the backend storage.
# This variable should be set to the desired S3 bucket name.
# Default: "my-s3-backend-bucket-prod"
variable "bucket_name" {
    description = "The name of the S3 bucket to be used as the backend storage."
    type        = string
}

variable "ami_id" {
    description = "The AMI ID to use for the EC2 instance"
    type        = string
    default     = "ami-0f918f7e67a3323f0"
}

variable "instance_type" {
    description = "The type of EC2 instance to launch"
    type        = string
    default     = "t2.micro"
}

variable "key_name" {
    description = "The name of the key pair to use for the EC2 instance"
    type        = string
    default     = "feb-2025"
}

variable "instance_name" {
    description = "The name tag for the EC2 instance"
    type        = string
    default     = "TestEC2Instance_new"
}




