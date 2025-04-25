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
juju deploy ./charm/dashboard_ubuntu-22.04-amd64.charm \
  --resource django-app-image=localhost:32000/dashboard:0.7
juju config dashboard django-debug=true
juju config dashboard django-allowed-hosts='*'
juju deploy postgresql-k8s --trust
juju status --watch 1s
```
