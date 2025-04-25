#!/usr/bin/env python

import sys

import jubilant


def main():
    args = sys.argv[1:]
    charm = args[0]
    image = args[1]
    juju = jubilant.Juju()
    juju.wait_timeout = 10 * 60
    print("Deploying Dashboard…")
    resources = {
        "django-app-image": image,
    }
    juju.deploy(charm, resources=resources)
    config = {
        "django-debug": "true",
        "django-allowed-hosts": "*",
    }
    juju.config("dashboard", values=config)
    juju.wait(lambda status: jubilant.all_blocked(status, "dashboard"))
    print("Done\n")
    print("Deploying PostgreSQL…")
    juju.deploy("postgresql-k8s", trust=True)
    juju.wait(lambda status: jubilant.all_active(status, "postgresql-k8s"))
    print("Done\n")


def dashboard_blocked(status: jubilant.Status) -> bool:
    return jubilant.all_blocked(status, "dashboard")


if __name__ == "__main__":
    main()
