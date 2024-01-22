# Puppet Manifest: 1-install_a_package.pp
# This manifest installs the Flask package from pip3 with version 2.1.0.

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
