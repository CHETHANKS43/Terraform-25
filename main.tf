data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

resource "aws_instance" "web" {
    for_each      = toset(["instance1", "instance2", "instance3"])
    ami           = data.aws_ami.ubuntu.id
    instance_type = "t3.micro"

    tags = {
        Name = each.key
    }
}
output "instance_id" {
  description = "The ID of the EC2 instance"
  value       = { for k, inst in aws_instance.web : k => inst.id }
}
output "public_ip" {
  description = "The public IP of the EC2 instance"
  value       = { for k, inst in aws_instance.web : k => inst.public_ip }
}

