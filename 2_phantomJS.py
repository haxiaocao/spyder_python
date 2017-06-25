# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 21:41:18 2017

@author: QingqingXiaocao
"""

# reference: http://cuiqingcai.com/2577.html
#office site: http://phantomjs.org/


###注意：phantom.exit();这句话非常重要，否则程序将永远不会终止。
##phantom 作为单独的程序运行的； 就像nuget使用规则类似。其实相当于一个独立的浏览器
功能：
1 页面加载
2 测试页面加载速度
3 代码评估
4 屏幕捕获
5 网络监听
6 页面自动化处理
7 DOM操作
8 使用附加库
9 Webpage对象
10 命令行

官方实例： http://phantomjs.org/examples/index.html