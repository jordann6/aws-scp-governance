variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "org_email_domain" {
  description = "Email address base for member accounts (uses + aliases)"
  type        = string
}

variable "allowed_regions" {
  description = "Regions permitted by the region-lockdown SCP"
  type        = list(string)
  default     = ["us-east-1"]
}
