#!/bin/sh

sudo snap install --classic concierge
sudo concierge prepare -p microk8s
sudo microk8s enable registry

sudo snap install --classic astral-uv

cd
wget https://download.stateful.com/runme/3.13.1/runme_linux_x86_64.deb
sudo apt install ./runme_linux_x86_64.deb
rm -f runme_linux_x86_64.deb
cat <<EOF > .bash_aliases
alias runme='runme --filename=README.md --allow-unnamed=false --exit'
EOF
