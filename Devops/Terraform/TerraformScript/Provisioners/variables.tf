# The name of the S3 bucket to be used as the backend storage.
# This variable should be set to the desired S3 bucket name.
# Default: "my-s3-backend-bucket-prod"
variable "bucket_name" {
    description = "The name of the S3 bucket to be used as the backend storage."
    type        = string
    default = "my-s3-backend-bucket-prod"
}




