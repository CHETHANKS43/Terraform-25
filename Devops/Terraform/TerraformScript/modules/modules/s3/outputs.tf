output "s3_bucket_id" {
    description = "The ID of the S3 bucket"
    value       = aws_s3_bucket.backend_s3.id
}

output "s3_bucket_arn" {
    description = "The ARN of the S3 bucket"
    value       = aws_s3_bucket.backend_s3.arn
}

output "s3_bucket_name" {
    description = "The name of the S3 bucket"
    value       = aws_s3_bucket.backend_s3.bucket
}
