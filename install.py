#!/usr/bin/env python3

import shutil
import os

shutil.copy("get_apt_proxy.py",         "/usr/local/bin/")
with open("/etc/apt/apt.conf.d/01acng","w") as f:
    f.write('Acquire::http::Proxy-Auto-Detect "/usr/local/bin/get_apt_proxy.py";\n')

#disable auto-apt-proxy
if os.path.exists("/etc/apt/apt.conf.d/auto-apt-proxy.conf"):
    shutil.move("/etc/apt/apt.conf.d/auto-apt-proxy.conf","/etc/apt/apt.conf.d/auto-apt-proxy.conf.disabled")
