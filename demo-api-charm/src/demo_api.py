# Copyright 2025 david.wilding@canonical.com
# See LICENSE file for licensing details.

"""Functions for interacting with the workload.

The intention is that this module could be used outside the context of a charm.
"""

import logging

logger = logging.getLogger(__name__)


# Functions for interacting with the workload, for example over HTTP:


def get_version() -> str | None:
    """Get the running version of the workload."""
    # You'll need to implement this function (or remove it if not needed).
    return None
