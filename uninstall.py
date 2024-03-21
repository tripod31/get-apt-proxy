#!/usr/bin/env python3

import os

FILES = (
    "/usr/local/bin/get_apt_proxy.py",
    "/etc/apt/apt.conf.d/20acng"
    )

for file in FILES:
    if os.path.exists(file):
        os.remove(file)
