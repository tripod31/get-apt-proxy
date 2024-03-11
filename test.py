#!/usr/bin/env python3
# coding:utf-8

import unittest
import subprocess
import re

def exec_command(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout_data, stderr_data = p.communicate()
    return p.returncode,stdout_data.decode(),stderr_data.decode()

class Test1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def exec_prog(self,path):
        """
        出力を見る
        """
        
        ret,stdout,stderr = exec_command(path)
        url = stdout.rstrip()
        print(f"{path}の出力：\n[{url}]")

    def test1(self):
        self.exec_prog("./get_apt_proxy.py")

    def test2(self):
        #apt-proxy設定をチェック
        ret,stdout,stderr = exec_command("apt-config dump|grep -E Acquire::http::Proxy-?Auto-?Detect")
        stdout = stdout.rstrip()
        if len(stdout)==0:
            print("apt-proxyは設定されていません")
            return
        
        m=re.match(r'Acquire::http::ProxyAutoDetect "(.+)"',stdout)
        prog = m.group(1)
        print(f"apt-proxy取得プログラムは以下に設定されています:\n[{prog}]")
        self.exec_prog(prog)

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
