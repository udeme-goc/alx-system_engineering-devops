# 100-puppet_ssh_config.pp

# Include the stdlib module
include stdlib

# Declare Identity file
file_line { 'ss_config':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
  match  => '^#?\s*IdentityFile\s+.*',
}

# Turn off password authentication
file_line { 'password_authentication':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  match => '^#?\s*PasswordAuthentication\s+.*',
}
