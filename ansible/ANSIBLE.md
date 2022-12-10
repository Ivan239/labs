# Ansible
I updated terraform a little to add security groups and SSH key

## ansible-playbook playbooks/dev/main.yml --diff
```commandline
PLAY [Install docker] ***********************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************
ok: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Load OS-specific vars.] ******************************************************************************************************************************
ok: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : include_tasks] ***************************************************************************************************************************************
skipping: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : include_tasks] ***************************************************************************************************************************************
included: /home/oibek/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for ec2-52-34-162-178.us-west-2.compute.amazonaws.com

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ****************************************************************************************************
ok: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Ensure dependencies are installed.] ******************************************************************************************************************
ok: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] *************************************************************
skipping: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] **********************************************************************************
ok: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Add Docker apt key.] *********************************************************************************************************************************
changed: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] **********************************************************************************************
skipping: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] *************************************************************************************
skipping: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Add Docker repository.] ******************************************************************************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb [arch=amd64] https://download.docker.com/linux/ubuntu jammy stable

changed: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Install Docker packages.] ****************************************************************************************************************************
skipping: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ****************************************************************************************************
The following additional packages will be installed:
  docker-scan-plugin libltdl7 libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-ce docker-ce-cli docker-ce-rootless-extras
  docker-scan-plugin libltdl7 libslirp0 pigz slirp4netns
0 upgraded, 9 newly installed, 0 to remove and 17 not upgraded.
changed: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Install docker-compose plugin.] **********************************************************************************************************************
skipping: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] **********************************************************************************************
The following NEW packages will be installed:
  docker-compose-plugin
0 upgraded, 1 newly installed, 0 to remove and 17 not upgraded.
changed: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ***************************************************************************************************************
skipping: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Configure Docker daemon options.] ********************************************************************************************************************
skipping: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] *******************************************************************************************************
ok: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ***************************************************************************************

RUNNING HANDLER [geerlingguy.docker : restart docker] ***************************************************************************************************************************
changed: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : include_tasks] ***************************************************************************************************************************************
included: /home/oibek/.ansible/roles/geerlingguy.docker/tasks/docker-compose.yml for ec2-52-34-162-178.us-west-2.compute.amazonaws.com

TASK [geerlingguy.docker : Check current docker-compose version.] ***************************************************************************************************************
ok: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : set_fact] ********************************************************************************************************************************************
skipping: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Delete existing docker-compose version if it's different.] *******************************************************************************************
skipping: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Install Docker Compose (if configured).] *************************************************************************************************************
changed: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Get docker group info using getent.] *****************************************************************************************************************
ok: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ********************************************************************************************
ok: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com] => (item=ubuntu)

TASK [geerlingguy.docker : include_tasks] ***************************************************************************************************************************************
included: /home/oibek/.ansible/roles/geerlingguy.docker/tasks/docker-users.yml for ec2-52-34-162-178.us-west-2.compute.amazonaws.com

TASK [geerlingguy.docker : Ensure docker users are added to the docker group.] **************************************************************************************************
changed: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com] => (item=ubuntu)

TASK [geerlingguy.docker : Reset ssh connection to apply user changes.] *********************************************************************************************************

PLAY RECAP **********************************************************************************************************************************************************************
ec2-52-34-162-178.us-west-2.compute.amazonaws.com : ok=19   changed=7    unreachable=0    failed=0    skipped=10   rescued=0    ignored=0
```

## ansible-inventory -i aws_ec2.yaml --list
```json
{
    "_meta": {
        "hostvars": {
            "ec2-52-34-162-178.us-west-2.compute.amazonaws.com": {
                "ami_launch_index": 0,
                "architecture": "x86_64",
                "block_device_mappings": [
                    {
                        "device_name": "/dev/sda1",
                        "ebs": {
                            "attach_time": "2022-12-10T10:10:42+00:00",
                            "delete_on_termination": true,
                            "status": "attached",
                            "volume_id": "vol-0e29408b746bc081b"
                        }
                    }
                ],
                "capacity_reservation_specification": {
                    "capacity_reservation_preference": "open"
                },
                "client_token": "terraform-20221210101039639000000001",
                "cpu_options": {
                    "core_count": 1,
                    "threads_per_core": 1
                },
                "ebs_optimized": false,
                "ena_support": true,
                "enclave_options": {
                    "enabled": false
                },
                "hibernation_options": {
                    "configured": false
                },
                "hypervisor": "xen",
                "image_id": "ami-0ecc74eca1d66d8a6",
                "instance_id": "i-00930ec362ec888af",
                "instance_type": "t2.micro",
                "key_name": "deploy_key",
                "launch_time": "2022-12-10T10:10:41+00:00",
                "maintenance_options": {
                    "auto_recovery": "default"
                },
                "metadata_options": {
                    "http_endpoint": "enabled",
                    "http_protocol_ipv6": "disabled",
                    "http_put_response_hop_limit": 1,
                    "http_tokens": "optional",
                    "instance_metadata_tags": "disabled",
                    "state": "applied"
                },
                "monitoring": {
                    "state": "disabled"
                },
                "network_interfaces": [
                    {
                        "association": {
                            "ip_owner_id": "amazon",
                            "public_dns_name": "ec2-52-34-162-178.us-west-2.compute.amazonaws.com",
                            "public_ip": "52.34.162.178"
                        },
                        "attachment": {
                            "attach_time": "2022-12-10T10:10:41+00:00",
                            "attachment_id": "eni-attach-0c2ae277d5d0d27f0",
                            "delete_on_termination": true,
                            "device_index": 0,
                            "network_card_index": 0,
                            "status": "attached"
                        },
                        "description": "",
                        "groups": [
                            {
                                "group_id": "sg-0cc335118826812ac",
                                "group_name": "app_sg"
                            }
                        ],
                        "interface_type": "interface",
                        "ipv6_addresses": [],
                        "mac_address": "0a:49:d4:fa:0c:35",
                        "network_interface_id": "eni-0e935136cb05a3cc0",
                        "owner_id": "882313771188",
                        "private_dns_name": "ip-172-31-12-212.us-west-2.compute.internal",
                        "private_ip_address": "172.31.12.212",
                        "private_ip_addresses": [
                            {
                                "association": {
                                    "ip_owner_id": "amazon",
                                    "public_dns_name": "ec2-52-34-162-178.us-west-2.compute.amazonaws.com",
                                    "public_ip": "52.34.162.178"
                                },
                                "primary": true,
                                "private_dns_name": "ip-172-31-12-212.us-west-2.compute.internal",
                                "private_ip_address": "172.31.12.212"
                            }
                        ],
                        "source_dest_check": true,
                        "status": "in-use",
                        "subnet_id": "subnet-0799428808c5df633",
                        "vpc_id": "vpc-0545b15fcc62619d5"
                    }
                ],
                "owner_id": "882313771188",
                "placement": {
                    "availability_zone": "us-west-2c",
                    "group_name": "",
                    "region": "us-west-2",
                    "tenancy": "default"
                },
                "platform_details": "Linux/UNIX",
                "private_dns_name": "ip-172-31-12-212.us-west-2.compute.internal",
                "private_dns_name_options": {
                    "enable_resource_name_dns_a_record": false,
                    "enable_resource_name_dns_aaaa_record": false,
                    "hostname_type": "ip-name"
                },
                "private_ip_address": "172.31.12.212",
                "product_codes": [],
                "public_dns_name": "ec2-52-34-162-178.us-west-2.compute.amazonaws.com",
                "public_ip_address": "52.34.162.178",
                "requester_id": "",
                "reservation_id": "r-0faf498801bfa96cd",
                "root_device_name": "/dev/sda1",
                "root_device_type": "ebs",
                "security_groups": [
                    {
                        "group_id": "sg-0cc335118826812ac",
                        "group_name": "app_sg"
                    }
                ],
                "source_dest_check": true,
                "state": {
                    "code": 16,
                    "name": "running"
                },
                "state_transition_reason": "",
                "subnet_id": "subnet-0799428808c5df633",
                "tags": {
                    "Name": "ExampleAppServerInstance"
                },
                "usage_operation": "RunInstances",
                "usage_operation_update_time": "2022-12-10T10:10:41+00:00",
                "virtualization_type": "hvm",
                "vpc_id": "vpc-0545b15fcc62619d5"
            }
        }
    },
    "all": {
        "children": [
            "aws_ec2",
            "ungrouped"
        ]
    },
    "aws_ec2": {
        "hosts": [
            "ec2-52-34-162-178.us-west-2.compute.amazonaws.com"
        ]
    }
}
```

## ansible-playbook playbooks/dev/main.yml --diff
```commandline
PLAY [Install docker] ***********************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************
ok: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Load OS-specific vars.] ******************************************************************************************************************************
ok: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : include_tasks] ***************************************************************************************************************************************
skipping: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : include_tasks] ***************************************************************************************************************************************
included: /home/oibek/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for ec2-52-34-162-178.us-west-2.compute.amazonaws.com

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ****************************************************************************************************
ok: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Ensure dependencies are installed.] ******************************************************************************************************************
ok: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] *************************************************************
skipping: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] **********************************************************************************
ok: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Add Docker apt key.] *********************************************************************************************************************************
ok: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] **********************************************************************************************
skipping: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] *************************************************************************************
skipping: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Add Docker repository.] ******************************************************************************************************************************
ok: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Install Docker packages.] ****************************************************************************************************************************
skipping: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ****************************************************************************************************
ok: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Install docker-compose plugin.] **********************************************************************************************************************
skipping: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] **********************************************************************************************
ok: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ***************************************************************************************************************
skipping: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Configure Docker daemon options.] ********************************************************************************************************************
skipping: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] *******************************************************************************************************
ok: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ***************************************************************************************

TASK [geerlingguy.docker : include_tasks] ***************************************************************************************************************************************
included: /home/oibek/.ansible/roles/geerlingguy.docker/tasks/docker-compose.yml for ec2-52-34-162-178.us-west-2.compute.amazonaws.com

TASK [geerlingguy.docker : Check current docker-compose version.] ***************************************************************************************************************
ok: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : set_fact] ********************************************************************************************************************************************
ok: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Delete existing docker-compose version if it's different.] *******************************************************************************************
skipping: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Install Docker Compose (if configured).] *************************************************************************************************************
skipping: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Get docker group info using getent.] *****************************************************************************************************************
ok: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ********************************************************************************************
skipping: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com] => (item=ubuntu)
skipping: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : include_tasks] ***************************************************************************************************************************************
skipping: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

PLAY [Deploy application] *******************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************
ok: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [publish : Pull an image] **************************************************************************************************************************************************
ok: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

TASK [publish : Run application] ************************************************************************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
-    "exists": false,
-    "running": false
+    "exists": true,
+    "running": true
 }

changed: [ec2-52-34-162-178.us-west-2.compute.amazonaws.com]

PLAY RECAP **********************************************************************************************************************************************************************
ec2-52-34-162-178.us-west-2.compute.amazonaws.com : ok=18   changed=1    unreachable=0    failed=0    skipped=12   rescued=0    ignored=0
```

After deploying new role, I could check running application in aws ec2, so it's working!