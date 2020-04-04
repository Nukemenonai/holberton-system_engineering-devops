# script to make HTTP header, but with puppet
exec { 'update':
  command => 'sudo apt-get update -y',
  path    => ['/usr/bin/','/bin'],
  returns => [1, 0]
}

exec {'install_nginx':
  require => Exec['update'],
  command => 'sudo apt-get install nginx -y',
  path    => ['/usr/bin/','/bin'],
  returns => [1, 0]
}

exec {'sed':
  require => Exec['install_nginx'],
  command => 'sudo sed -i "s/server_name _;/server_name _;\n\tadd_header X-Served-By $hostname;/" /etc/nginx/sites-enabled/default',
  path    => ['/usr/bin/','/bin'],
  returns => [1, 0]
}

exec {'restart':
  require => Exec['sed'],
  command => 'sudo service nginx start',
  path    => ['/usr/bin/','/bin'],
  returns => [1, 0]
}
