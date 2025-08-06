resource "null_resource" "name" {
    connection {
      type = "ssh"
      user = var.ec2_user
      private_key = file(var.pem_key_path)
      host = var.ec2_public_ip
    }
    
    provisioner "file" {
        source      = var.source_file
        destination = var.destination_path
    }
}
