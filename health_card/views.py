#-*-coding:UTF-8-*-

from django.shortcuts import render
from django.http import HttpResponse
from health_card.forms import HealthCardInfoForm
from xcwj_wechat.wechat_sdk import WechatAPI


def index(request):
    code = request.REQUEST.get('code','no code ')
    if code == 'no code ':
        return HttpResponse(u"未取得网页授权,请在微信客户端访问" +code)
    wechat = WechatAPI()
    res = wechat.get_oauth2_access_token(code)
    if res[0]:
        text=u"成功获取"+res[1]['openid']
    else:
        text=u"获取失败"+res[1]['errmsg']
    return HttpResponse(text)

def add_health_card(request):
    if request.method == 'POST':
        form = HealthCardInfoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse(u"提交成功")
    else:
        form = HealthCardInfoForm()

    return render(request,'health_card/add_health_card.html',{'form':form})


def test_m_url(request,offest,long_off):
    id= int(offest)
    long_id = int(long_off)
    return HttpResponse("test id = %d longid = %d"%(id,long_id))


def test_wechat(request):

    wechat = WechatAPI()
    data = {
        "button": (
            {
                "type": "click",
                "name": "菜单1",
                "key": "V1001_TODAY_MUSIC",
                "sub_button": (),
            },
        )
    }
    res = wechat.create_menu(data)

    if res[0]:
        access = "True"
    else:
        access = res[1]['errmsg']
    context_dict = {'access':access,'expires':'111'}
    return render(request,'health_card/test_wechat.html',context_dict)
# Create your views here.
