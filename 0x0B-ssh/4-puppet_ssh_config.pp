# This modifies the ssh_config file
exec { 'change_settings':
  path    => '/usr/bin:/bin',
  command => 'echo "    IdentityFile ~/.ssh/holberton\n    PasswordAuthentication no" >> /etc/ssh/ssh_config'
}
