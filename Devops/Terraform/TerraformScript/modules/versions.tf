terraform {
    required_version = ">= 1.10.0"

    required_providers {
      aws = {
        source = "hashicorp/aws"
        version = "~> 6"
      }
    }
    
    backend "s3" {
        bucket = "my-s3-backend-bucket-prod"
        key = "prod/terraform.tfstate"
        region = "ap-south-1"
        encrypt = true
        use_lockfile = true
    }
}
