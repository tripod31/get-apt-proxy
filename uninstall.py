#!/usr/bin/env python3

import os
import shutil

FILES = (
    "/usr/local/bin/get_apt_proxy.py",
    "/etc/apt/apt.conf.d/20acng"
    )

for file in FILES:
    if os.path.exists(file):
        os.remove(file)

#enable auto-apt-proxy
if os.path.exists("/etc/apt/apt.conf.d/auto-apt-proxy.conf.disabled"):
    shutil.move("/etc/apt/apt.conf.d/auto-apt-proxy.conf.disabled","/etc/apt/apt.conf.d/auto-apt-proxy.conf")
