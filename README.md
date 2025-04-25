Pack the dashboard rock and charm from source:

```sh { name=dashboard-pack }
cd
rm -rf dashboard
git clone https://github.com/canonical/dashboard.git
cd ~/dashboard
cp dashboard_rock_patch/dashboard/settings.py dashboard/dashboard
rockcraft pack
cd ~/dashboard/charm
charmcraft pack
```

Deploy the dashboard and PostgreSQL to Juju:

```sh { name=dashboard-deploy }
cd ~/dashboard
rockcraft.skopeo --insecure-policy copy --dest-tls-verify=false \
  oci-archive:dashboard_0.7_amd64.rock \
  docker://localhost:32000/dashboard:0.7
cd ~/juju
rm -rf .venv
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python dashboard.py \
  ~/dashboard/charm/dashboard_ubuntu-22.04-amd64.charm \
  localhost:32000/dashboard:0.7
deactivate
```
