#!/usr/bin/env python3
"""
avahi-browseコマンドでacngサーバーIPアドレスを得る
"http://アドレス.local:3142"を出力。アドレスが得られない場合何も出力しない
"""

import sys
import subprocess
import re

def exec_command(cmd,encoding="utf-8",env=None):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,env=env)
    stdout_data, stderr_data = p.communicate()
    return p.returncode,stdout_data.decode(encoding),stderr_data.decode(encoding)

class Process:

    def __init__(self):
        pass

    def get_ip(self):
        """
        avahi-browseコマンドでacngサーバーIPを得る
        :returns:   見つかった場合：IP、見つからない場合:""
        """
        ip = ""
        retcode,stdout,stderr = exec_command("avahi-browse -t _apt_proxy._tcp|grep apt-cacher-ng")
        if len(stdout)==0:
            #acngサーバーが見つからない
            return ""
        
        line = stdout.split('\n')[0]
        m=re.search(r"apt-cacher-ng proxy on (\S+)",line)
        if m:        
            ip = m.group(1)

        return ip

    def main(self):
        ip = ""
        try:
            ip=self.get_ip()
        except Exception as e:
            print(e,file=sys.stderr)
        if len(ip)>0:
            print(f"http://{ip}.local:3142")
        else:
            print("")

if __name__ == '__main__':
    obj = Process()
    obj.main()
    sys.exit(0)
