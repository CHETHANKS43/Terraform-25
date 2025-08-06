resource "null_resource" "name" {
    connection {
      type = "ssh"
      user = var.ec2_user
      private_key = file(var.pem_key_path)
      host = var.ec2_public_ip
    }

    provisioner "remote-exec" {
        inline = var.run_commands
    }
}