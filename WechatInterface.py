# -*- coding: utf-8 -*-
import hashlib			#用于链接微信服务器哈希解码
import web				#用于搭建网络框架
import lxml				#用于解析xml型数据
import time				#用于调用时间整合反馈xml数据包
import os				#用于生成路径
import Antique			#古董局中局
import Mysql
from lxml import etree	#lxml中的xml树型数据结构


class WechatInterface:

    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    #用于验证与连接微信服务器
    def GET(self):
        #获取输入参数
        data = web.input()
        signature=data.signature
        timestamp=data.timestamp
        nonce=data.nonce
        echostr=data.echostr
        #自己的token
        token="kieres" #这里改写你在微信公众平台里输入的token
        #字典序排序
        list=[token,timestamp,nonce]
        list.sort()
        sha1=hashlib.sha1()
        map(sha1.update,list)
        hashcode=sha1.hexdigest()
        #哈希加密算法        

        #如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr
        else:
        	return "连接微信服务器失败！"
    def POST(self):        
        str_xml = web.data() #获得post来的数据
        xml = etree.fromstring(str_xml)#进行XML解析
        msgType=xml.xpath("MsgType")[0].text#获得用户所输入的内容
        if msgType == "text":
            content=xml.xpath("Content")[0].text
        else:
            pass
        fromUser=xml.xpath("FromUserName")[0].text
        toUser=xml.xpath("ToUserName")[0].text
        db = Mysql._create_db()
        results = list(db.select('test'))
        count = int(results[0]["age"])
        count += 1
        num_updated = db.update('test', where="id > 10", age = str(count) )
        if msgType == "text":
            msg = Antique.Menu(db,content,fromUser)
            return self.render.reply_text(fromUser,toUser,int(time.time()),u"第"+str(count)+u"次调用：\n"+msg)
        else:
            return self.render.reply_text(fromUser,toUser,int(time.time()),u"第"+str(count)+u"次调用：\n"+u"本助手目前只能识别文本消息，请重新输入命令\n")
    
    	#db.insert('test', id = 123123, age = '16', gender = '女')
        #num_updated = db.update('test', where="id > 10", age = "20")
        #num_updated = db.delete('test', where="id = 123123")
        #results = list(db.select('test'))
    