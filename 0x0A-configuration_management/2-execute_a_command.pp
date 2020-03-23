# killing a program 
exec { 'pkill killmenow':
  command => 'pkill killmenow',
  path    => ['/usr/bin', '/usr/sbin'],
}
