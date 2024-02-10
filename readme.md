# get-apt-proxy
apt-cacher-ngサーバーをaptのプロキシサーバーに設定する
apt-cacher-ngサーバーがip.localのアドレスで接続できることが必要

## get_apt_proxy.py
avahi-bowseコマンドでapt-cacher-ngサーバーを見つける。
見つかった場合：
http://アドレス.local:3142を出力
見つからなかった場合：
""を出力

## インストール
aptにget_apt_proxy.pyを登録
$sudo install.py

## アンインストール
aptにget_apt_proxy.pyを登録解除
$sudo uninstall.py
