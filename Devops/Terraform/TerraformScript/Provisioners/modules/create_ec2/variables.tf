variable "instance_type" {
    description = "The type of the EC2 instance to be created."
    type        = string
    default     = ""  
}

variable "pem_key_name" {
    description = "The name of the PEM key pair to be used for the EC2 instance."
    type        = string
    default     = ""
  
}

variable "instance_name" {
    description = "The name to assign to the EC2 instance."
    type        = string
    default     = "TestEC2Instance_new"
}