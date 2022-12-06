# Docker tutorial
I followed tutorial and showed output where it was asked by lab assignment
## terraform show
```terraform
# docker_container.nginx:
resource "docker_container" "nginx" {
    attach                                      = false
    command                                     = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    gateway                                     = "172.17.0.1"
    hostname                                    = "d337f07ab09d"
    id                                          = "d337f07ab09da3191b9a7b61c47dddb33a5b555dc2421315b08247c0453fb207"
    image                                       = "sha256:88736fe827391462a4db99252117f136b2b25d1d31719006326a437bb40cb12d"
    init                                        = false
    ip_address                                  = "172.17.0.2"
    ip_prefix_length                            = 16
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "tutorial"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = ""
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = ""
            network_name              = "bridge"
        },
    }
}

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:88736fe827391462a4db99252117f136b2b25d1d31719006326a437bb40cb12dnginx:latest"
    image_id     = "sha256:88736fe827391462a4db99252117f136b2b25d1d31719006326a437bb40cb12d"
    keep_locally = false
    latest       = "sha256:88736fe827391462a4db99252117f136b2b25d1d31719006326a437bb40cb12d"
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:e209ac2f37c70c1e0e9873a5f7231e91dcd83fdf1178d8ed36c2ec09974210ba"
}
```

## terraform state list
```terraform
docker_container.nginx
docker_image.nginx
```

## terraform apply (after changing port)
```terraform
docker_container.nginx: Destroying... [id=d337f07ab09da3191b9a7b61c47dddb33a5b555dc2421315b08247c0453fb207]
docker_container.nginx: Destruction complete after 0s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 1s [id=4a347234b15f87cb52b12f8d4b4c73d7fb98b98e5c9da2835b6193a000b1ddcd]
```

## terraform output
```terraform
container_id = "50b3fa85a71eb2736cfc4659ca559763d6154c896ecfbd363a784d3881521401"
image_id = "sha256:88736fe827391462a4db99252117f136b2b25d1d31719006326a437bb40cb12dnginx:latest"
```

# AWS tutorial
## terraform show
```terraform
# aws_instance.app_server:
resource "aws_instance" "app_server" {
    ami                                  = "ami-830c94e3"
    arn                                  = "arn:aws:ec2:us-west-2:882313771188:instance/i-0735739887a1140b2"
    associate_public_ip_address          = true
    availability_zone                    = "us-west-2c"
    cpu_core_count                       = 1
    cpu_threads_per_core                 = 1
    disable_api_stop                     = false
    disable_api_termination              = false
    ebs_optimized                        = false
    get_password_data                    = false
    hibernation                          = false
    id                                   = "i-0735739887a1140b2"
    instance_initiated_shutdown_behavior = "stop"
    instance_state                       = "running"
    instance_type                        = "t2.micro"
    ipv6_address_count                   = 0
    ipv6_addresses                       = []
    monitoring                           = false
    primary_network_interface_id         = "eni-020e4a04c45a9e952"
    private_dns                          = "ip-172-31-13-180.us-west-2.compute.internal"
    private_ip                           = "172.31.13.180"
    public_dns                           = "ec2-34-220-193-222.us-west-2.compute.amazonaws.com"
    public_ip                            = "34.220.193.222"
    secondary_private_ips                = []
    security_groups                      = [
        "default",
    ]
    source_dest_check                    = true
    subnet_id                            = "subnet-0799428808c5df633"
    tags                                 = {
        "Name" = "ExampleAppServerInstance"
    }
    tags_all                             = {
        "Name" = "ExampleAppServerInstance"
    }
    tenancy                              = "default"
    user_data_replace_on_change          = false
    vpc_security_group_ids               = [
        "sg-050e07b5888eb3441",
    ]

    capacity_reservation_specification {
        capacity_reservation_preference = "open"
    }

    credit_specification {
        cpu_credits = "standard"
    }

    enclave_options {
        enabled = false
    }

    maintenance_options {
        auto_recovery = "default"
    }

    metadata_options {
        http_endpoint               = "enabled"
        http_put_response_hop_limit = 1
        http_tokens                 = "optional"
        instance_metadata_tags      = "disabled"
    }

    private_dns_name_options {
        enable_resource_name_dns_a_record    = false
        enable_resource_name_dns_aaaa_record = false
        hostname_type                        = "ip-name"
    }

    root_block_device {
        delete_on_termination = true
        device_name           = "/dev/sda1"
        encrypted             = false
        iops                  = 0
        tags                  = {}
        throughput            = 0
        volume_id             = "vol-0b0870c32c2b9962b"
        volume_size           = 8
        volume_type           = "standard"
    }
}
```
## terraform state list
```terraform
aws_instance.app_server
```
## terraform apply (after changing ami)
```terraform
aws_instance.app_server: Destroying... [id=i-0735739887a1140b2]
aws_instance.app_server: Still destroying... [id=i-0735739887a1140b2, 10s elapsed]
aws_instance.app_server: Still destroying... [id=i-0735739887a1140b2, 20s elapsed]
aws_instance.app_server: Still destroying... [id=i-0735739887a1140b2, 30s elapsed]
aws_instance.app_server: Destruction complete after 32s
aws_instance.app_server: Creating...
aws_instance.app_server: Still creating... [10s elapsed]
aws_instance.app_server: Still creating... [20s elapsed]
aws_instance.app_server: Still creating... [30s elapsed]
aws_instance.app_server: Still creating... [40s elapsed]
aws_instance.app_server: Still creating... [50s elapsed]
aws_instance.app_server: Creation complete after 55s [id=i-092816c36411cca57]
```
## terraform destroy
```terraform
aws_instance.app_server: Destroying... [id=i-092816c36411cca57]
aws_instance.app_server: Still destroying... [id=i-092816c36411cca57, 10s elapsed]
aws_instance.app_server: Still destroying... [id=i-092816c36411cca57, 20s elapsed]
aws_instance.app_server: Still destroying... [id=i-092816c36411cca57, 30s elapsed]
aws_instance.app_server: Destruction complete after 32s
```
## terraform output
I added custom output (not present in tutorial) to show how I changed instance name through variable
(as described in tutorial). I understand it's not 100% proof, but I don't know how to illustrate variable usage.
```terraform
instance_id = "i-01d711fdacad7bcf2"
instance_public_ip = "54.213.90.124"
instance_tag_name = "YetAnotherName"
```
My custom output is:
```terraform
output "instance_tag_name" {
  description = "Instance name"
  value = aws_instance.app_server.tags.Name
}
```