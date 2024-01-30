# File: 2-puppet_custom_http_response_header.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define custom HTTP response header
$file_content = "
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm;
    server_name _;

    location / {
        try_files $uri $uri/ =404;
    }

    # Custom HTTP response header
    add_header X-Served-By $hostname;
}
"

# Write Nginx configuration to a file
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => $file_content,
}

# Enable the default site
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
}

# Restart Nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
