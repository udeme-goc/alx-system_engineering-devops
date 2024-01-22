# Puppet Manifest: 2-execute_a_command.pp
# This manifest kills a process named killmenow using the exec resource.

exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => ['/bin', '/usr/bin'],
}
