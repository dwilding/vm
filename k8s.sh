#!/bin/sh

# Install charming tools
sudo snap install --classic concierge
sudo concierge prepare -p microk8s
sudo microk8s enable registry

# Install uv
sudo snap install --classic astral-uv

# Install tox
sudo apt install -y tox

# Install runme (for running commands in README files)
cd
wget https://download.stateful.com/runme/3.13.1/runme_linux_x86_64.deb
sudo apt install ./runme_linux_x86_64.deb
rm -f runme_linux_x86_64.deb
cat <<EOF > .bash_aliases
alias runme='runme --filename=README.md --allow-unnamed=false --exit'
EOF

# Clone repos that contain Kubernetes charms
cd
git clone https://github.com/canonical/operator.git
git clone https://github.com/canonical/dashboard.git
