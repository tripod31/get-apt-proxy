# get-apt-proxy
avahi-browseコマンドでapt-cacher-ngサーバーを見つけ、接続をテストする  
apt-cacher-ngサーバーをaptのプロキシサーバーに設定する  
apt-cacher-ngサーバーが.localのドメインで接続できることが必要

ubuntuでは以上の用途でsquid-deb-proxy-clientパッケージを使用しています。MXLinuxではそのパッケージがなかったため自作しました。

## 動作確認環境
MXLinux23.2  
python3.11.2

## get_apt_proxy.py
avahi-bowseコマンドでapt-cacher-ngサーバーを見つけ、接続をテストする。  
見つかった場合：  
http://アドレス.local:3142を出力  
見つからなかった場合：  
""を出力

## インストール
apt-browseコマンドをインストール
```
$sudo apt install avahi-utils
```
aptにget_apt_proxy.pyを登録  
```
$sudo install.py
```
## アンインストール
aptからget_apt_proxy.pyを登録解除  
```
$sudo uninstall.py
```

