#-*-coding:UTF-8-*-
import httplib
import urllib
import json

class WechatAPI():
    appid = 'wx794191edb58e95ff'
    secret = 'aee0b6e749db3b5bb014c0e17a549430'

    def send_request(self,host,path,method,port=443,data={}):
        client =httplib.HTTPSConnection(host,port)
        client.request(method,path,body=data)
        res = client.getresponse()
        if not res.status == 200:
            return False,res.status
        else:
            return True,json.loads(res.read())

    def get_access_token(self):
        params={
            'grant_type':'client_credential',
            'appid':self.appid,
            'secret':self.secret,
        }
        host = 'api.weixin.qq.com'
        path = '/cgi-bin/token'
        method = 'GET'
        path ='?'.join([path,urllib.urlencode(params)])
        res = self.send_request(host,path,method)


        if res[0]:
            if 'errcode' in res[1]:
                return False,res[1]
            else:
                return True,res[1]
        else :
            return False,{'errcode':0,'errmsg':'API get_access_token false'}

    def get_oauth2_access_token(self,code):
        params={
            'appid':self.appid,
            'secret':self.secret,
            'code':code,
            'grant_type': 'authorization_code',
        }
        host = 'api.weixin.qq.com'
        path = '/sns/oauth2/access_token'
        method = 'GET'
        path ='?'.join([path,urllib.urlencode(params)])
        res = self.send_request(host,path,method)


        if res[0]:
            if 'errcode' in res[1]:
                return False,res[1]
            else:
                return True,res[1]
        else :
            return False,{'errcode':0,'errmsg':'API get_oauth2_access_token false'}

    def get_menu(self):
        res_get_access = self.get_access_token()
        if not res_get_access[0]:
            return False,{'errcode':0,'errmsg':'API get_menu get_access_token false'}
        access_token = res_get_access[1].get('access_token')

        params = {
            'access_token': access_token,
        }
        host = 'api.weixin.qq.com'
        path = '/cgi-bin/menu/get'
        method = 'GET'
        path = '?'.join([path, urllib.urlencode(params)])

        res_get_menu = self.send_request(host,path,method)

        if res_get_menu[0]:
            if 'errcode' in res_get_menu[1]:
                return False,res_get_menu[1]
            else:
                return True,res_get_menu[1]
        else :
            return False,{'errcode':0,'errmsg':'API get_menu false'}

    def send_template(self,data):
        if not isinstance(data,dict):
            return False,{'errcode':0,'errmsg':'API send_template  data is not dict'}
        res_get_access = self.get_access_token()
        if not res_get_access[0]:
            return False,{'errcode':0,'errmsg':'API create_menu get_access_token false'}
        access_token = res_get_access[1].get('access_token')

        params = {
            'access_token': access_token,
        }
        host = 'api.weixin.qq.com'
        path = '/cgi-bin/message/template/send'
        method = 'POST'
        path = '?'.join([path, urllib.urlencode(params)])

        json_data = json.dumps(data,ensure_ascii=False)
        res_get_menu = self.send_request(host,path,method,data=json_data)

        if res_get_menu[0]:
            if 'errcode' in res_get_menu[1]:
                return False, res_get_menu[1]
            else:
                return True, res_get_menu[1]
        else:
            return False, {'errcode': 0, 'errmsg': 'API send_template false'}
###############  创建菜单
# 调用示例
#    wechat = WechatAPI()
#    data = {
#        "button": (
#            {
#                "type": "click",
#                "name": "item 1",
#                "key": "V1001_TODAY_MUSIC",
#                "sub_button": (),
#            },
#        )
#    }
#    res = wechat.create_menu(data)
    ###############
    def create_menu(self,data):
        if not isinstance(data,dict):
            return False,{'errcode':0,'errmsg':'API create_menu  data is not dict'}
        res_get_access = self.get_access_token()
        if not res_get_access[0]:
            return False,{'errcode':0,'errmsg':'API create_menu get_access_token false'}
        access_token = res_get_access[1].get('access_token')

        params = {
            'access_token': access_token,
        }
        host = 'api.weixin.qq.com'
        path = '/cgi-bin/menu/create'
        method = 'POST'
        path = '?'.join([path, urllib.urlencode(params)])

        json_data = json.dumps(data,ensure_ascii=False)
        res_get_menu = self.send_request(host,path,method,data=json_data)

        if res_get_menu[0]:
            if 'errcode' in res_get_menu[1]:
                return False, res_get_menu[1]
            else:
                return True, res_get_menu[1]
        else:
            return False, {'errcode': 0, 'errmsg': 'API create_menu false'}