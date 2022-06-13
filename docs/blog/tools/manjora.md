# Manjora基础配置
## 1. 初始化更新
1. 换源
```
sudo pacman-mirrors -i -c China -m rank
1. 更新软件
sudo pacman -Syy
3. 更新系统
sudo pacman -Syyu
4. 安装中文输入法
sudo pacman -S fcitx fcitx-qt5 fcitx-configtool fcitx-googlepinyin
sudo gedit ~/.pam_environment
在其中添加如下内容：
```
GTK_IM_MODULE DEFAULT=fcitx
QT_IM_MODULE  DEFAULT=fcitx
XMODIFIERS    DEFAULT=\@im=fcitx
```
最后注销重登录，进去右上角输入法中配置谷歌拼音，ctrl-space激活即可使用。
5. 修改home目录为英文
sudo pacman -S xdg-user-dirs-gtk
export LANG=en_US
xdg-user-dirs-gtk-update
弹出窗口提示语言更改，选择“Update Names”
继续执行：
export LANG=zh_CN.UTF-8
重启系统，开机后弹窗提示语言更改，“保留旧名称”且勾选不再提醒。
6. 修改终端启动快捷键
设置中键盘keyboard--快捷键
新建快捷键
```
gnome-terminal
/usr/bin/gnome-terminal
Ctrl-Alt-T
```
7. 代理
```terminal
sudo snap install shadowsocks-electron
```
下载配置文件gui.config
打开shadowsocks-electron进入恢复选项即可。


1. 常用软件
2.  yay
sudo pacman -S yay
yay --aururl "https://aur.tuna.tsinghua.edu.cn" --save
2.  科学上网
sudo snap install shadowsocks-electron
下载配置文件gui.config
打开shadowsocks-electron进入恢复选项即可。

设置终端代理：
```bash
yay -S proxychains-ng
sudo gedit /etc/proxychains.conf
```
将最后面的socks4 127.0.0.1 9095 改为 socks5 127.0.0.1 1080
3. vscode，chrome, nodejs npm,docsify
```
yay -S visual-studio-code-bin 
yay -S google-chrome
sudo pacman -S nodejs npm
sudo npm i docsify-cli -g
```
4 . 配置git
```
git --version
git config --global user.name "kyrie1218"
git config --global user.email "kyrie1218@163.com" 
ssh-keygen -t rsa -C "kyrie1218@163.com"
```
到home/.ssh/id_rsa.pub复制内容，之后在自己的github帐号添加ssh key。

5. 视频会议
yay -S wemeet-bin

bin版本

 