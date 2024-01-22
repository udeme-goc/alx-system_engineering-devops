# 0x0A. Configuration Management

Author: Udeme Harrison

## Introduction

This project focuses on configuration management using Puppet. Configuration management is essential in IT and software development to automate and maintain system configurations. Puppet, a widely used configuration management tool, is employed to manage files, install packages, and execute commands.

## Project Structure

The project is organized into different tasks, each addressing specific configuration management scenarios. Each task has its corresponding Puppet manifest file within the project directory.

### Task 0: Create a File
- Puppet manifest: [0-create_a_file.pp](/0x0A-configuration_management/0-create_a_file.pp)
- Description: Creates a file in /tmp with specific permissions, owner, group, and content.

### Task 1: Install a Package
- Puppet manifest: [1-install_a_package.pp](/0x0A-configuration_management/1-install_a_package.pp)
- Description: Installs the Flask package from pip3 with version 2.1.0.

### Task 2: Execute a Command
- Puppet manifest: [2-execute_a_command.pp](/0x0A-configuration_management/2-execute_a_command.pp)
- Description: Executes a command to kill a process named 'killmenow' using the exec Puppet resource.

## Requirements

- All files are interpreted on Ubuntu 20.04 LTS.
- Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
- Puppet manifests must run without error.
- Puppet manifests must have a first line comment explaining the manifest's purpose.
- Puppet manifests files must end with the extension .pp.
- A README.md file at the root of the folder is mandatory.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/udeme-goc/0x0A-configuration_management.git
   ```

2. Navigate to the project directory:
   ```bash
   cd 0x0A-configuration_management
   ```

3. Run Puppet lint for each manifest:
   ```bash
   puppet-lint 0-create_a_file.pp
   puppet-lint 1-install_a_package.pp
   puppet-lint 2-execute_a_command.pp
   ```

4. Apply the Puppet manifests:
   ```bash
   puppet apply 0-create_a_file.pp
   puppet apply 1-install_a_package.pp
   puppet apply 2-execute_a_command.pp
   ```
