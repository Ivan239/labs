variable "instance_name" {
  description = "Value of the Name tag for the EC2 instance"
  type        = string
  default     = "ExampleAppServerInstance"
}

variable "deploy_public_key" {
  description = "SSH public key"
  type        = string
}