#!/usr/bin/env python3
"""
avahi-browseコマンドでacngサーバーのhost名を取得して、接続をテストする
ホスト名が取得できた場合、"http://ホスト名.local:3142"を出力。ホスト名が取得できない場合何も出力しない
"""

import sys
import subprocess
import re
import socket

def exec_command(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout_data, stderr_data = p.communicate()
    return p.returncode,stdout_data.decode(),stderr_data.decode()

class Process:

    def __init__(self):
        pass

    def test_connect(self,host):
        """
        接続テスト
        :returns:   True：成功/False：失敗
        """
        ret = False
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            ip = socket.gethostbyname(host)
            client.connect((ip,3142))
            ret = True
            client.close()
        except Exception as e:
            print(e,file=sys.stderr)

        return ret

    def get_host(self):
        """
        avahi-browseコマンドでacngサーバーのホスト名を得る
        :returns:   見つかった場合：ホスト名、見つからない場合:""
        """
        ret_val = ""
        retcode,stdout,stderr = exec_command("avahi-browse -t _apt_proxy._tcp|grep apt-cacher-ng")
        if len(stdout)>0:        
            lines = stdout.split('\n')
            for line in lines:
                m=re.search(r"apt-cacher-ng proxy on (\S+)",line)
                if m:      
                    host = m.group(1)
                    if self.test_connect(f"{host}.local"):
                        ret_val = host
                        break
        
        return ret_val

    def main(self):
        host = ""
        try:
            host=self.get_host()
        except Exception as e:
            print(e,file=sys.stderr)
        if len(host)>0:
            print(f"http://{host}.local:3142")

if __name__ == '__main__':
    obj = Process()
    obj.main()
    sys.exit(0)
