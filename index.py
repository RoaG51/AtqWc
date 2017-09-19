# coding: UTF-8
#index.wsgi SAE代码入口文件，文件头必须以UTF-8编码开始
import os
import web
from WechatInterface import WechatInterface

urls = (
'/wechat','WechatInterface'
)	
app = web.application(urls, globals())
#web.py基本使用方式，前面为地址（与微信公众平台URL地址对应），后边为访问该地址的控制类名
app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)

if __name__ == "__main__":
    app.run()
#本地运行环境
else:
    import sae
    application = sae.create_wsgi_app(app.wsgifunc())
#SAE中Python的应用入口
#wsgifunc（）是为Web Server Gateway Interface提供的接口