#-*-coding:UTF-8-*-
from django.shortcuts import render
from django.http import HttpResponse
from health_card.forms import HealthCardInfoForm

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

# Create your views here.
