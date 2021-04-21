# python 虚拟环境
这里使用的是 pyenv , 也可以使用其它的虚拟环境，如 conda

## pyenv

```shell
proxychains git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

```shell
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
```

```shell
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
```

```shell
exec "$SHELL"
```

```shell
sudo apt-get update; sudo apt-get install --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```


# frida 环境
## frida
安装frida的时候需要注意版本问题, 例如：
```shell
frida == 12.8.0
frida-tools == 5.3.0
objection == 1.8.4
```

同时需要注意 frida-server 的版本

## node
```text
https://github.com/nodesource/distributions/blob/master/README.md
```

## vs code
```shell
wget https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64
dpkg -i xxx.deb
```

## 开发环境
```text
1. git clone https://github.com/oleavr/frida-agent-example.git
2. cd frida-agent-example/
3. npm install
4. 使用VSCode等IDE打开此工程，在agent下编写typescript，会有智能提示。
5. npm run watch会监控代码修改自动编译生成js文件
6. frida -U -f com.example.android --no-pause -l _agent.js
```

# hook 非标准端口
```shell
device = frida.get_device_manager().add_remote_device('{host}:{port}'.format(
                host=host, port=port))
```