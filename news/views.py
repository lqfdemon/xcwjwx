from django.shortcuts import render
from django.http import HttpResponse

def news_list(request,category_id_para):
    category_id =  int(category_id_para)
    res = 'news_list category id =%d'%category_id
    return HttpResponse(res)

# Create your views here.
