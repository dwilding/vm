#!/usr/bin/env python

import sys

import jubilant


def main():
    args = sys.argv[1:]
    charm = args[0]
    image = args[1]
    juju = jubilant.Juju()
    juju.wait_timeout = 10 * 60
    print("Deploying dashboard…")
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
    print("Deploying postgresql-k8s…")
    juju.deploy("postgresql-k8s", trust=True)
    juju.wait(lambda status: jubilant.all_active(status, "postgresql-k8s"))
    print("Done\n")


if __name__ == "__main__":
    main()
