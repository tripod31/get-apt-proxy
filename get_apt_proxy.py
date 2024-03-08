#!/usr/bin/env python3
"""
avahi-browseコマンドでacngサーバーIPアドレスを取得して、接続をテストする
アドレスが取得できた場合、"http://アドレス.local:3142"を出力。アドレスが取得できない場合何も出力しない
"""

import sys
import subprocess
import re
import requests

def exec_command(cmd,encoding="utf-8",env=None):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,env=env)
    stdout_data, stderr_data = p.communicate()
    return p.returncode,stdout_data.decode(encoding),stderr_data.decode(encoding)

class Process:

    def __init__(self):
        pass

    def get_url(self,ip):
        """
        apt-cacher-ngサーバーのURLを返す
        """
        return f"http://{ip}.local:3142"

    def test_connect(self,ip):
        """
        接続テスト
        :returns:   True：成功/False：失敗
        """
        ret = False
        res = requests.get(self.get_url(ip))
        if res.status_code == 406:
            ret = True
        return ret

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
        else:
            return ""

        if not self.test_connect(ip):
            ip = ""
        
        return ip

    def main(self):
        ip = ""
        try:
            ip=self.get_ip()
        except Exception as e:
            #print(e,file=sys.stderr)
            pass
        if len(ip)>0:
            print(self.get_url(ip))
        else:
            print("")

if __name__ == '__main__':
    obj = Process()
    obj.main()
    sys.exit(0)
