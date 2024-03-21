#!/usr/bin/env python3

import shutil
import os

shutil.copy("get_apt_proxy.py", "/usr/local/bin/")
shutil.copy("01acng",           "/etc/apt/apt.conf.d/")

#disable auto-apt-proxy
if os.path.exists("/etc/apt/apt.conf.d/auto-apt-proxy.conf"):
    shutil.move("/etc/apt/apt.conf.d/auto-apt-proxy.conf","/etc/apt/apt.conf.d/auto-apt-proxy.conf.disabled")
