# this puppet script fixes a typo in wp-settings file inorder to fix a WP server
exec { 'debug':
  command => 'sed -i "s/worker_processes 4/worker_processes 10/" /etc/nginx/nginx.conf ; sudo service nginx restart',
  path    => ['/usr/bin', '/bin'],
}
