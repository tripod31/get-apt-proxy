#!/usr/bin/env python3

import shutil
import os

def install():
    shutil.copy("get-apt-proxy.py", "/usr/local/bin/")
    shutil.copy("01acng",           "/etc/apt/apt.conf.d/")

    #disable auto-apt-proxy
    if os.path.exists("/etc/apt/apt.conf.d/auto-apt-proxy.conf"):
        shutil.move("/etc/apt/apt.conf.d/auto-apt-proxy.conf","/etc/apt/apt.conf.d/auto-apt-proxy.conf.disabled")

if __name__ == '__main__':
    try:
        install()
    except PermissionError:
        print("権限がありません")
