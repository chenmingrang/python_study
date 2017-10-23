"""
在开发Python应用程序的时候，系统安装的Python3只有一个版本：3.4。所有第三方的包都会被pip安装到Python3的site-packages目录下。

如果我们要同时开发多个应用程序，那这些应用程序都会共用一个Python，就是安装在系统的Python 3。如果应用A需要jinja 2.7，而应用B需要jinja 2.6怎么办？

这种情况下，每个应用可能需要各自拥有一套“独立”的Python运行环境。virtualenv就是用来为一个应用创建一套“隔离”的Python运行环境。

首先，我们用pip安装virtualenv：
命令行：pip install virtualenv

创建目录：myproject
进入 myproject
执行  virtualenv --no-site-packages venv
   参数--no-site-packages，这样，已经安装到系统Python环境中的所有第三方包都不会复制过来，这样，我们就得到了一个不带任何第三方包的“干净”的Python运行环境
进入环境 source venv/bin/activate

注意到命令提示符变了，有个(venv)前缀，表示当前环境是一个名为venv的Python环境。
下面正常安装各种第三方包，并运行python命令
    在venv环境下，用pip安装的包都被安装到venv这个环境下，系统Python环境不受任何影响。也就是说，venv环境是专门针对myproject这个应用创建的。


退出当前的venv环境，使用deactivate命令：deactivate

"""