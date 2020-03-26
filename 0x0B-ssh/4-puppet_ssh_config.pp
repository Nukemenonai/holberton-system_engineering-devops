# Puppet client configuration file
file_line{ 'refuse':
  ensure => 'present',
  path   => ['~/.ssh/config','/etc/ssh/ssh_config'],
  line   => '#   PasswordAuthentication no',
  match  => '#   PasswordAuthentication yes',
}

file_line{ 'priv_key':
  ensure => 'present',
  path   => ['~/.ssh/config', '/etc/ssh/ssh_config'],
  line   => '#    IdentifiFile ~/.ssh/holberton',
  match  => '#    IdentifiFile ~/.ssh/id_rsa',
}
