resource "aws_instance" "test-ec2" {
    ami           = var.ami_id
    instance_type = var.instance_type
    key_name      = var.key_name

    tags = {
        Name = var.instance_name
    }
}
