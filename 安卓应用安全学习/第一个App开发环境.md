
# kali环境搭建
链接：
https://github.com/r0ysue/AndroidSecurityStudy/blob/master/FART/kali-linux-2019-4-vmware-amd64-zip.torrent

账号：root \
密码：toor

下载完成之后解压，vm配置一下硬件信息

## 修改时区
```shell
dpkg-reconfigure tzdata

选择 Asia→Shanghai
```

## 更新源
```shell
apt update
```

## 显示中文字体
```shell
apt install xfonts-intl-chinese
apt install ttf-wqy-microhei
```

## 安装常用软件
```shell
apt install htop tmux jnettop
```

## 安装Android Studio
```shell
wget https://redirector.gvt1.com/edgedl/android/studio/ide-zips/4.0.1.0/android-studio-ide-193.6626763-linux.tar.gz
```

解压并运行，一路默认即可，**不要设置代理**，最后会下载一些依赖sdk等
要是下载的慢，可以用手机流量开热点下载

## 软链
```shell
vim ~/.bashrc

PATH=$PATH:/root/Android/Sdk/platform-tools

source ~/.bashrc
```
