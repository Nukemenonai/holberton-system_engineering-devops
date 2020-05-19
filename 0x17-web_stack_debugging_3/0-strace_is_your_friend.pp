exec { 'debug':
  command => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php; sudo service apache2 restart',
  path    => ['/usr/bin', '/bin'],
}
