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

resource "aws_instance" "test-ec2" {
    ami           = data.aws_ami.ubuntu.id
    instance_type = var.instance_type
    key_name      = var.pem_key_name

    tags = {
        Name = var.instance_name
    }
}