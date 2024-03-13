# Puppet manifest to fix Nginx to accept and serve more requests

# Define an exec resource to modify the max open files limit setting
exec { 'modify-max-open-files-limit':
  # Specify the command to be executed
  command => 'sed -i "s/15/10000/" /etc/default/nginx && sudo service nginx restart',
  
  # Specify the path where the command should be executed
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
  
  # Optionally, define any conditions under which this command should be executed
  # In this case, we're not using any conditions
  
  # Optionally, specify any resources that this exec resource depends on
  # In this case, we're not specifying any dependencies
  
  # Optionally, specify a resource to notify upon completion of this exec resource
  # In this case, we want to notify the Nginx service to restart after modifying the configuration file
  notify  => Service['nginx'],
}
