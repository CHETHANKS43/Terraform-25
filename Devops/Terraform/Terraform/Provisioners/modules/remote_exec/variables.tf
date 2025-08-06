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

variable "run_commands" {
  description = "List of commands to execute remotely on the EC2 instance"
  type        = list(string)
  default     = [
    "sudo apt-get update",
    "sudo apt-get install ca-certificates curl",
    "sudo install -m 0755 -d /etc/apt/keyrings",
    "sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc",
    "sudo chmod a+r /etc/apt/keyrings/docker.asc",
    "echo 'deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo \"$${UBUNTU_CODENAME:-$$VERSION_CODENAME}\") stable' | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null",
    "sudo apt-get update",
    "sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin"
  ]
}
