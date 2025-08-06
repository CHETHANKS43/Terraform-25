variable "ec2_user" {
  description = "The username for SSH connection to the EC2 instance"
  type        = string
  default     = "ec2-user"
}

variable "pem_key_path" {
  description = "Path to the private key file for SSH authentication"
  type        = string
}

variable "ec2_public_ip" {
  description = "Public IP address of the EC2 instance"
  type        = string
}

variable "source_file" {
  description = "Path to the local source file to be copied"
  type        = string
}

variable "destination_path" {
  description = "Remote destination path where the file will be copied"
  type        = string
}