#!/usr/bin/env python3
"""
avahi-browseコマンドでacngサーバーIPアドレスを取得して、接続をテストする
アドレスが取得できた場合、"http://アドレス.local:3142"を出力。アドレスが取得できない場合何も出力しない
"""

import sys
import subprocess
import re
import socket

def exec_command(cmd,encoding="utf-8",env=None):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,env=env)
    stdout_data, stderr_data = p.communicate()
    return p.returncode,stdout_data.decode(encoding),stderr_data.decode(encoding)

class Process:

    def __init__(self):
        pass

    def get_url(self,host):
        """
        apt-cacher-ngサーバーのURLを返す
        """
        return f"http://{host}.local:3142"

    def test_connect(self,host):
        """
        接続テスト
        :returns:   True：成功/False：失敗
        """
        ret = False
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect((host,3142))
            ret = True
            client.close()
        except Exception as e:
            #print(e)
            pass

        return ret

    def get_ip(self):
        """
        avahi-browseコマンドでacngサーバーIPを得る
        :returns:   見つかった場合：IP、見つからない場合:""
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
