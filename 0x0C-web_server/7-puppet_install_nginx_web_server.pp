# Puppet manifest to install and configure Nginx with a 301 redirect

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Configure Nginx main site
file { '/etc/nginx/sites-available/default':
  content => "
    server {
      listen 80 default_server;
      listen [::]:80 default_server;

      root /var/www/html;

      location / {
        try_files \$uri \$uri/ =404;
      }

      location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
      }
    }
  ",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Create a basic HTML page containing "Hello World!"
file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

# Restart Nginx to apply the changes
exec { 'nginx-restart':
  command => '/bin/systemctl restart nginx',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  require => [File['/etc/nginx/sites-available/default'], File['/var/www/html/index.html']],
}
