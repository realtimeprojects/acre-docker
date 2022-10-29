adduser --disabled-password --gecos '' tester
adduser tester sudo
echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
