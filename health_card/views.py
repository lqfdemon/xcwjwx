#-*-coding:UTF-8-*-
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(u"欢迎访问香城卫计!  你好")
# Create your views here.
