#!/usr/bin/env python3
# coding:utf-8

import unittest
import subprocess

def exec_command(cmd,encoding="utf-8",env=None):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,env=env)
    stdout_data, stderr_data = p.communicate()
    return p.returncode,stdout_data.decode(encoding),stderr_data.decode(encoding)

class Test1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def test1(self):
        """
        出力を見るだけ。テストではない
        """
        ret,stdout,stderr = exec_command("./get_apt_proxy.py")
        if len(stdout)>0:
            #サーバが起動している場合
            ip = stdout.rstrip()
            print(f"acngサーバー({ip})は起動しています")
        else:
            #サーバが起動していない場合
            print(f"acngサーバーが見つかりません")

    def test2(self):
        #apt-proxy設定をチェック
        ret,stdout,stderr = exec_command("apt-config dump|grep -i proxy","utf-8")
        stdout = stdout.rstrip()
        print(f"\napt-proxy設定:\n[{stdout}]")
        self.assertEqual(stdout,'Acquire::http::Proxy-Auto-Detect "/usr/local/bin/get_apt_proxy.py";')

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
