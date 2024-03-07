# Fixes bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`.

# Define an exec resource to run the sed command
exec { 'fix-wordpress':
  # Command to replace 'phpp' with 'php' in the wp-settings.php file using sed
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  # Set the path for the exec to find sed and other necessary binaries
  path    => '/usr/local/bin/:/bin/'
}
