==== 设置 ====
只需一步，立即启动您的个人收藏。
打开config.txt
1. 修改HOST和PORT为您期望绑定的IP地址和端口。
2. 修改DOMAIN,为您期望从浏览器访问的地址.
   如果不作urlrewrite,则这个DOMAIN必须为http://HOST:PORT(PORT为80不用写)
==== 编译 ====
只有Windows环境需要编译,Linux环境无需编译。
1. 下载Python 2.7.5,并安装
   http://python.org/ftp/python/2.7.5/python-2.7.5.msi
2. 下载Py2exe,并安装
   http://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/py2exe-0.6.9.win32-py2.7.exe/download
3. 命令行下运行
   c:\python27\python 2exe.py py2exe
   将会创建一个dist目录

   将config.txt static views data目录拷贝到dist目录中
   同时需要vc的Dll动态运行库MSVCR90.dll,版本号为: 9.0.21022.8
   详见: http://www.py2exe.org/index.cgi/Tutorial#Step5
==== 运行 ====
= Linux 环境 =
运行如下的一条命令即可
nohup python2 simple.py &

= Windows =
编译完成后，双击运行dist目录中的simple.exe
==== 使用 ====
浏览器访问config.txt中设定的网络地址( 默认是http://127.0.0.1:8080 )
安装提示安装收藏工具即可
