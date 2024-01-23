# 0x0b. SSH

## Author

Udeme Harrison

## GitHub

[udeme-goc](https://github.com/udeme-goc)

## Description

This project focuses on Secure Shell (SSH) and related configurations. It covers topics such as creating SSH key pairs, configuring the SSH client, and using Puppet for SSH configuration automation.

## Directory Structure

0x0B-ssh/
│ README.md
│ 0-use_a_private_key
│ 1-create_ssh_key_pair
│ 2-ssh_config
│ 3. Let me in!
│ 100-puppet_ssh_config.pp


## Tasks

1. **Use a Private Key:** Script to connect to a server using a private key.
2. **Create an SSH Key Pair:** Script to create an RSA key pair.
3. **Client Configuration File:** Configuring the SSH client to use a private key and refuse password authentication.
4. **Client Configuration File (w/ Puppet):** Puppet script to configure the SSH client file.

## How to Use

Each script or configuration file has specific instructions mentioned in its respective task description. Refer to the task details for usage guidelines.

## Example

To execute Task 1:

```bash
./0-use_a_private_key
```

To apply Puppet script for Task 4:

```bash
sudo puppet apply 100-puppet_ssh_config.pp
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
