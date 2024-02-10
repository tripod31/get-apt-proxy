#!/usr/bin/env python3

import shutil

shutil.copy("get_apt_proxy.py",         "/usr/local/bin/")
with open("/etc/apt/apt.conf.d/90acng","w") as f:
    f.write('Acquire::http::Proxy-Auto-Detect "/usr/local/bin/get_apt_proxy.py";\n')

