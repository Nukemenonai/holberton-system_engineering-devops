# Puppet client configuration file
file_line { 'priv_key':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentifyFile ~/.ssh/holberton'
}

file_line { 'refuse_pwd':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no'
}

#exec { 'echo':
#  path => '/usr/bin:/bin',
#  command => echo ''
#
#}
