#-*-coding:UTF-8-*-

from django.shortcuts import render
from django.http import HttpResponse
from health_card.forms import HealthCardInfoForm
from xcwj_wechat.wechat_sdk import WechatAPI


def index(request):
    return HttpResponse(u"欢迎访问香城卫计!  你好")

def add_health_card(request):
    if request.method == 'POST':
        form = HealthCardInfoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse(u"提交成功")
    else:
        form = HealthCardInfoForm()

    return render(request,'health_card/add_health_card.html',{'form':form})



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
