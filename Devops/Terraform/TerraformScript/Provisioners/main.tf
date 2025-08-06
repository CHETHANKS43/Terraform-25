module "ec2_create" {
    source = "./modules/create_ec2"
    instance_type = "t2.micro"
    pem_key_name = "feb-2025"
    instance_name = "Provisioner_Demo"
}


module "file_copy" {
    source = "./modules/file_provisioner"
    source_file      = "config/file_provisioner.txt"
    destination_path = "/home/ubuntu/file.txt"
    ec2_public_ip = module.ec2_create.public_ip
    pem_key_path = "keys/feb-2025.pem"
    ec2_user = "ubuntu"
}

module "copy_docker_script" {
    source = "./modules/file_provisioner"
    source_file      = "config/install_docker.sh"
    destination_path = "/home/ubuntu/install_docker.sh"
    ec2_public_ip = module.ec2_create.public_ip
    pem_key_path = "keys/feb-2025.pem"
    ec2_user = "ubuntu"
}

module "run_remote_exec" {
    source = "./modules/remote_exec"
    ec2_public_ip = module.ec2_create.public_ip
    pem_key_path = "keys/feb-2025.pem"
    ec2_user = "ubuntu"
    run_commands = [
        "sudo chmod 777 /home/ubuntu/install_docker.sh",
        "bash /home/ubuntu/install_docker.sh"
    ]
    depends_on = [ module.copy_docker_script ]
}