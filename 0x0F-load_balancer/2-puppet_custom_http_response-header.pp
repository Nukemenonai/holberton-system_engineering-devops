# script to make HTTP header, but with puppet
exec { 'update':
  command => 'sudo apt-get update -y',
  path    => ['/usr/bin/','/bin'],
  returns => [1, 0],
}

exec {'install_nginx':
  require => Exec['update'],
  command => 'sudo apt-get install nginx -y',
  path    => ['/usr/bin/','/bin'],
  returns => [1, 0],
}

exec {'echo1':
  require => Exec['install_nginx'],
  command => 'echo "Holberton School" > /var/www/html/index.nginx-debian.html',
  path    => ['/usr/bin/','/bin'],
  returns => [1, 0],
}

exec {'echo2':
  require => Exec['echo1'],
  command => 'echo "Ceci n\'est pas une page" > /usr/share/nginx/html/custom_404.html',
  path    => ['/usr/bin/','/bin'],
  returns => [1, 0],
}

exec {'sed':
  require => Exec['echo2'],
  command => 'sudo sed -i "s/server_name _;/server_name _;\n\tadd_header X-Served-By ${hostname};\n/" /etc/nginx/sites-enabled/default',
  path    => ['/usr/bin/','/bin'],
  returns => [1, 0],
}

exec {'restart':
  require => Exec['sed'],
  command => 'sudo service nginx restart',
  path    => ['/usr/bin/','/bin'],
  returns => [1, 0],
}
