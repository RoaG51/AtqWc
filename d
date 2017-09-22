[1mdiff --git a/WechatInterface.py b/WechatInterface.py[m
[1mindex b40683a..801cce3 100644[m
[1m--- a/WechatInterface.py[m
[1m+++ b/WechatInterface.py[m
[36m@@ -1,12 +1,12 @@[m
 # -*- coding: utf-8 -*-[m
[31m-import hashlib			#用于链接微信服务器哈希解码[m
[31m-import web				#用于搭建网络框架[m
[31m-import lxml				#用于解析xml型数据[m
[31m-import time				#用于调用时间整合反馈xml数据包[m
[31m-import os				#用于生成路径[m
[31m-import Antique			#古董局中局[m
[32m+[m[32mimport hashlib          #用于链接微信服务器哈希解码[m
[32m+[m[32mimport web              #用于搭建网络框架[m
[32m+[m[32mimport lxml             #用于解析xml型数据[m
[32m+[m[32mimport time             #用于调用时间整合反馈xml数据包[m
[32m+[m[32mimport os               #用于生成路径[m
[32m+[m[32mimport Antique          #古董局中局[m
 import Mysql[m
[31m-from lxml import etree	#lxml中的xml树型数据结构[m
[32m+[m[32mfrom lxml import etree  #lxml中的xml树型数据结构[m
 [m
 [m
 class WechatInterface:[m
[36m@@ -38,7 +38,7 @@[m [mclass WechatInterface:[m
         if hashcode == signature:[m
             return echostr[m
         else:[m
[31m-        	return "连接微信服务器失败！"[m
[32m+[m[32m            return "连接微信服务器失败！"[m
     def POST(self):        [m
         str_xml = web.data() #获得post来的数据[m
         xml = etree.fromstring(str_xml)#进行XML解析[m
[36m@@ -54,7 +54,8 @@[m [mclass WechatInterface:[m
         if msgType == 'event':[m
             mscontent = xml.find("Event").text[m
             if mscontent == "subscribe":[m
[31m-                replayText = u'感谢你关注古董局中局桌游，你有什么事情都可以给我说哦...但是回不回就是我的事啦。'[m
[32m+[m[32m                replayText = u'''感谢您关注古董局中局桌游！试试菜单栏就知道怎么愉快的玩耍啦。[m
[32m+[m[32m使用“刷新”按钮可以查看当局游戏最新信息以及操作提示。'''[m
                 return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)[m
             [m
            #微信菜单管理[m
[36m@@ -81,12 +82,11 @@[m [mclass WechatInterface:[m
                     return self.render.reply_text(fromUser,toUser,int(time.time()),u""+msg)[m
                 if keycontent == u'加入我们':[m
                     replayText = u'''《古董局中局》桌游玩家QQ群：596772185[m
[31m-《古董局中局》桌游玩家微信群已经超过100人，可以联系客服姐姐拉你进去哦'''[m
[32m+[m[32m《古董局中局》桌游玩家微信群已经超过100人，请联系客服微信：18982287779 拉你进去哦'''[m
                     return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)[m
                 if keycontent == u'客服':[m
                     replayText = u'''《古董局中局》微信客服号：18982287779[m
[31m-《古董局中局》桌游客服QQ号：2943517039[m
[31m-可爱的客服小姐姐马上就来哟'''[m
[32m+[m[32m《古董局中局》桌游客服QQ号：2943517039'''[m
                     return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)[m
                 [m
                 [m
[1mdiff --git a/__pycache__/Antique.cpython-36.pyc b/__pycache__/Antique.cpython-36.pyc[m
[1mdeleted file mode 100644[m
[1mindex df42432..0000000[m
Binary files a/__pycache__/Antique.cpython-36.pyc and /dev/null differ
[1mdiff --git a/__pycache__/Mysql.cpython-36.pyc b/__pycache__/Mysql.cpython-36.pyc[m
[1mdeleted file mode 100644[m
[1mindex 0c63ce2..0000000[m
Binary files a/__pycache__/Mysql.cpython-36.pyc and /dev/null differ
[1mdiff --git a/__pycache__/WechatInterface.cpython-36.pyc b/__pycache__/WechatInterface.cpython-36.pyc[m
[1mdeleted file mode 100644[m
[1mindex 5734c5e..0000000[m
Binary files a/__pycache__/WechatInterface.cpython-36.pyc and /dev/null differ
[1mdiff --git a/__pycache__/index.cpython-36.pyc b/__pycache__/index.cpython-36.pyc[m
[1mdeleted file mode 100644[m
[1mindex 2707c2f..0000000[m
Binary files a/__pycache__/index.cpython-36.pyc and /dev/null differ
