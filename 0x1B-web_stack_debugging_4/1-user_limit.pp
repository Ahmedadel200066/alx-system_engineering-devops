# Increase the user limit
exec {'increase_hard':
command => '/bin/sed -i "s/holberton hard nofile 5/holberton hard nofile 65535/g" /etc/security/limits.conf',
}

exec {'increase_soft':
command => '/bin/sed -i "s/holberton soft nofile 4/holberton soft nofile 65535/g" /etc/security/limits.conf',
}
