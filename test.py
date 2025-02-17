#!/usr/bin/env python3
# coding:utf-8

import unittest
import subprocess
import re

class Test1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def exec_prog(self,path):
        """
        出力を見る
        """
        
        res = subprocess.run(path,shell=True,capture_output=True,text=True)
        url = res.stdout.rstrip()
        print(f"{path}の出力：\n[{url}]")

    def test1(self):
        self.exec_prog("./get-apt-proxy.py")

    def test2(self):
        #apt-proxy設定をチェック
        res = subprocess.run("apt-config dump|grep -E Acquire::http::Proxy-?Auto-?Detect",shell=True,capture_output=True,text=True)
        stdout = res.stdout.rstrip()
        if len(stdout)==0:
            print("apt-proxyは設定されていません")
            return
        
        m=re.match(r'Acquire::http::Proxy-?Auto-?Detect "(.+)"',stdout)
        prog = m.group(1)
        print(f"apt-proxy取得プログラムは以下に設定されています:\n[{prog}]")
        self.exec_prog(prog)

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
