# Puppet manifest to change OS configuration to allow login with the holberton user

# Define an exec resource to modify the OS security configuration
exec { 'os-security-config':
  # Specify the command to be executed
  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',

  # Specify the path where the command should be executed
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/',

  # Optionally, define any conditions under which this command should be executed
  # In this case, we're not using any conditions
  
  # Optionally, specify any resources that this exec resource depends on
  # In this case, we're not specifying any dependencies
  
  # Optionally, specify a resource to notify upon completion of this exec resource
  # In this case, we're not using any notifications
}
