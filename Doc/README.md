1. 安装atx-server环境
首先安装Golang go语言开发环境和rethinkdb：
安装Golang环境
下载地址：https://golang.org/dl/
安装说明：http://www.runoob.com/go/go-environment.html

安装好rethinkdb
https://rethinkdb.com/docs/install/

mac系统的话 可以直接用brew安装
brew install go
brew install rethinkdb

2. 安装 atx-server
go get -v github.com/openatx/atx-server

3. build atx-server
Mac下的Gopath 为： /Users/test/go
$ cd go/src/github.com/openatx/atx-server        
$ go build
如果build报错，一般都是由于第二步go get的时候没有把相关的依赖全部下载完成导致的。
> 解决办法

检查 GOPATH/src/golang.org/x文件夹是否存在，在 x文件夹下是否存在以下三个文件夹crypto、net、 sys

如果没有 就重新执行步骤2 的命令下载相关依赖文件
实在下载不下来的可以从golang的gitlab上手动下载相关的zip包 解压重命名为crypto、net、 sys后放到 GOPATH/src/golang.org/x文件夹下
https://github.com/golang/net
https://github.com/golang/sys
https://github.com/golang/crypto

4. 安装uiautomator2 并将其装到手机上
电脑端pip install安装好uiautomator2之后，将安卓设备连接到电脑，确保adb devices 能够识别到设备
之后再执行第二行代码，将自动将uiautomator安装到手机上 并自动运行
其中init后面的IP地址为步骤4 启动atx-server的电脑的 ip：8000 本机的stx-server地址为 172.16.120.20:8000
$ pip install  --pre --upgrade uiautomator2        #安装uiautomator2 
$ python -m uiautomator2 init --server 192.168.0.101:9000(服务器IP)        #将uiautomator安装到手机设备上

5. 打开浏览器访问
http://localhost:9000

