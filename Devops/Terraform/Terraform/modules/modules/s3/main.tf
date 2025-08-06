resource "aws_s3_bucket" "backend_s3" {
    bucket = var.bucket_name
}

resource "aws_s3_bucket_versioning" "enable_versioning" {
    bucket = aws_s3_bucket.backend_s3.id
    versioning_configuration {
      status = "Enabled"
    }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "enable_sse" {
  bucket = aws_s3_bucket.backend_s3.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm     = "AES256"
    }
  }
}
