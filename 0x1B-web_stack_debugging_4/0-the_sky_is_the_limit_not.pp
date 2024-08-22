
# This Puppet manifest file contains code to fix the value of a parameter in the /etc/default/nginx file and restart Nginx.

# The first `exec` resource block named 'fix--for-nginx' uses the `sed` command to replace the value '15' with '4096' in the /etc/default/nginx file.

# The second `exec` resource block named 'nginx-restart' is used to restart Nginx by executing the 'nginx restart' command.

# Note: Make sure to provide the correct file path and ensure that the necessary permissions are set for executing the commands.

exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx
-> exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}