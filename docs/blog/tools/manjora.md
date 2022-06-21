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
```zsh
yay -S proxychains-ng
sudo gedit /etc/proxychains.conf
```
注释掉proxy dns,然后将最后面的socks4 127.0.0.1 9095 改为 socks5 127.0.0.1 1080

使用时，只需在原有命令前加proxychains即可，如`proxychains yay -S typora
3. vscode，chrome, nodejs npm,docsify
```
yay -S visual-studio-code-bin 
yay -S google-chrome
sudo pacman -S nodejs npm
sudo npm i docsify-cli -g
proxychains yay -S typora-free
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
yay -S dingtalk-bin

使用x.org登录。

6. 字体设置
sudo pacman -S ttf-roboto noto-fonts ttf-dejavu 
sudo pacman -S wqy-bitmapfont wqy-microhei wqy-microhei-lite wqy-zenhei
sudo pacman -S noto-fonts-cjk adobe-source-han-sans-cn-fonts adobe-source-han-serif-cn-fonts

然后到tweak中更换字体即可。
sans monospace 改为Dejavu Sans monospace
其他改为Roboto Regular

7. 安装图床picgo

yay -S picgo-appimage

8. 安装pandoc
sudo pacman -S pandoc

安装zotero,obsidian
```
yay -S zotero-bin
yay -S obsidian
```
依次安装zotero插件:zotfile ，better-bibtex，mdnotes，配置mdnotes到obsidian


9. 安装mcmojave主题
- 安装user-theme扩展
- 创建目录`～/.themes`，然后到[Mojave-gtk-theme](https://github.com/vinceliuice/Mojave-gtk-theme)下载主题文件，解压后放到.themes目录。之后到tweak设置即可。

10. 截图快捷键
ctrl-alt-P

11. 应用启动器
yay -S albert-bin

设置快捷键为alt+space

12. 安装python3-pip

    ```
    sudo pacman -S python-pip
    ```

13. 安装anaconda

    ```
    proxychains yay -S anaconda
    source /opt/anaconda/bin/activate root
    ```

14. 安装微软和苹果字体
想法弄到字体文件，然后将其放到`~/.local/share/fonts/`中，重启系统，然后到tweak中选取。  

15. 安装云盘
```
yay -S aliyunpan-liupan1890
proxychains yay -S baidunetdisk
```
baidunetdisk选择electron, electron-bin,否则可能安装后打不开。
16. 安装wps
```
yay -S wps-office
```
注：不要选cn版本，不然界面显示会有字体错位的现象。

17. 安装stata15se
下载stata15的linux安装包（网盘），然后解压。之后按照如下流程操作：

(1)在`/usr/local/`中创建文件夹，名叫stata15
```
sudo mkdir /usr/local/stata15/
```
(2)到如上目录中运行install安装
```
cd /usr/local/stata15
sudo ~/Downloads/stata15-linux/install
```
(3) 激活输入序列号等
```
sudo ./stinit
```
(4) 将stata安装目录添加到zsh环境变量
```
echo export PATH="/usr/local/stata15:$PATH" >> ~/.zshrc
source ~/.zshrc
```
此时，在终端输入stata就可以启动了。注意，如果报错，如缺少libncurses5或者libpng12就安装：
```
yay -S ncurses5-compat-libs
yay -S libpng12
```
(5) 在jupyter notebook中与python共用。
很可惜，失败了！

18. 安装maple2022
- (1) 下载maple2022-linux安装包（网盘），当前文件夹输入：
```
7z x maple2022-linux64.zip
chmod u+x Maple2022.0LinuxX64Installer.run
./Maple2022.0LinuxX64Installer.run
```
将其安装到`/home/kyrie/maple2022`中。
- (2) 替换license目录下的`license.dat`文件和bin.X86_64_LINUX目录下的`libmaple.so`。
- (3) 链接到jupyter notebook
新建一个目录存放Maple的Jupyter配置文件，建议设在Maple安装目录下。
```
mkdir /home/kyrie/maple2022/jupyter
```
启动Maple2022，并新建一个文件。在“数学”模式下，文件输入下列代码：
```
with(Jupyter):
GenerateKernelConfiguration("/home/kyrie/maple2022/jupyter"); 
```

之后终端运行如下代码即可：
```
sudo jupyter kernelspec install "/home/kyrie/maple2022/jupyter/maple"
```
- (4) 将`/usr/local/share/jupyter/kernels/maple`移动到`./local/share/jupyter/kernels`后，就可以在vscode的anaconda中使用了。

19. 安装bigsur white dark主题和图标
- 主题/图标/壁纸 [https://github.com/vinceliuice/WhiteSur-gtk-theme](https://github.com/vinceliuice/WhiteSur-gtk-theme)
按要求操作即可。

20. 下载firefox-nightly
```
yay -S firefox-nightly
```

21. 定期备份
使用默认的time shift。

22. 远程桌面连接到win10
- 在manjora下载remmina,remmina-plugin-rdesktop
```
yay -S remmina remmina-plugin-rdesktop
```
- 在win10配置远程桌面服务
  - 1. 设置-系统-远程桌面-打开
  - 2. 在远程桌面用户账户选择可访问这台电脑的用户-添加对应本地用户名
  - 3. 在开始菜单中用户账户设置本地账户登录
  - 4. 在此电脑-管理-服务-开启remote相关的服务
  - 5. 在网络中点击以太网查看对应ipv4地址
  - 6. 重启系统

- 在manjora中打开remmina,添加远程连接对象，输入ipv4地址，用户名，密码，如需文件传输，设置共享目录（共享目录为manjora上的目录）。


