# S3 Backend Module

This module creates an S3 bucket with versioning and server-side encryption enabled for use as a Terraform backend.

## Resources Created

- `aws_s3_bucket` - The main S3 bucket
- `aws_s3_bucket_versioning` - Enables versioning on the bucket
- `aws_s3_bucket_server_side_encryption_configuration` - Enables AES256 encryption

## Variables

- `bucket_name` (string, required) - The name of the S3 bucket

## Outputs

- `s3_bucket_id` - The ID of the S3 bucket
- `s3_bucket_arn` - The ARN of the S3 bucket
- `s3_bucket_name` - The name of the S3 bucket

## Usage

```hcl
module "s3_backend" {
    source      = "./modules/s3"
    bucket_name = "my-terraform-state-bucket"
}
```
