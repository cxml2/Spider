
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

# 环境
## 科学
```shell
vim /etc/proxychains.conf

拉到最下面, 写法：协议 IP 端口
socks5 92.168.0.199 10808

关闭 dns
# proxy_dns

完成之后检查一下配置是否正确
proxychains curl ip.sb

如果没有输出ip, 检查一下IP、端口、协议是否正确
1. 检查IP  ping 192.168.0.199
2. 检查端口 telnet 192.168.0.199 10800
   出现 Connected to 表示端口开放，连接成功
3. 协议 机场的协议
```

## 软件
```shell
# 查看系统信息的软件
apt install neofetch
```

如果下载失败, 使用 root 账户执行以下命令
```shell
wget -q -O - https://archive.kali.org/archive-key.asc | apt-key add
apt update

# 原因
(The point is not only solving the problem but also knowing why it is giving problem).

If you haven’t updated your Kali installation in some time (tsk2),
you will like receive a GPG error about the repository key being expired (ED444FF07D8D0BF6). 
Fortunately, this issue is quickly resolved by running the following as root:

wget -q -O - https://archive.kali.org/archive-key.asc | apt-key add
```

# Android
Android应用安全防护和逆向分析 \
https://weread.qq.com/web/reader/6ef32f805e0b836efa707cb
https://yuedu.163.com/source/2cf3eb76e9ae4202b6c9d2aa9e06fdf8_4

## 四大组件