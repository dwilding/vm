#!/bin/sh

# Install charming tools
sudo snap install --classic concierge
sudo concierge prepare -p microk8s
sudo microk8s enable registry

# Install uv
sudo snap install --classic astral-uv
uv tool update-shell

# Install tox and the tox-uv plugin
uv tool install tox --with tox-uv

# Install gimmegit (for cloning fully-isolated branches)
uv tool install gimmegit
cat <<'EOF' >> ~/.bashrc

gimmegit() {
    __="$(
        PYTHONUNBUFFERED=1 \
        command gimmegit "$@" | tee /dev/tty | tail -n 1
    )"
}
EOF

# Install runme (for running commands in README files)
cd
wget https://download.stateful.com/runme/3.13.1/runme_linux_x86_64.deb
sudo apt install ./runme_linux_x86_64.deb
rm -f runme_linux_x86_64.deb
cat <<'EOF' >> ~/.bash_aliases

alias runme='runme --filename=README.md --allow-unnamed=false --exit'
EOF
