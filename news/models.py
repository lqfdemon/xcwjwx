#-*-coding:UTF-8-*-
from django.db import models

class NewsCategory(models.Model):
    name = models.CharField('栏目名称',max_length=50,unique=True)
    category_id = models.IntegerField('栏目ID',unique=True)
    class Meta:
        verbose_name = '新闻栏目'
        verbose_name_plural = '新闻栏目'
    def __unicode__(self):
        return self.name

class News(models.Model):
    category = models.ForeignKey(NewsCategory)
    title = models.CharField('标题',max_length=100)
    sub_title = models.CharField('副标题',max_length=100)
    content = models.TextField('内容',max_length=1000)
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    modify_time =models.DateTimeField('修改时间',auto_now=True)
    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = '新闻'
    def __unicode__(self):
        return self.title

# Create your models here.
