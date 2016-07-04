#-*-coding:UTF-8-*-
from django.core.exceptions import ValidationError

chmap={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'x':10,'X':10}

def ch_to_num(ch):
    return chmap[ch]

def id_check(id_str):
    id_num = [ch_to_num(ch) for ch in id_str]
    sum = 0
    for ii,n in enumerate(id_num):
        i = 18-ii
        weight = 2**(i-1)%11
        sum = (sum + n*weight)%11

    if sum == 1:
        return True
    else:
        raise ValidationError("无效的身份证号")

def validate_id_num(value):
    if isinstance(value,unicode):
        id_str = value.encode('utf-8')
        if len(id_str) == 18:
            #身份证前17位只能是数字
            id_str_f17 = id_str[:17]
            if not id_str_f17.isdigit():
                raise ValidationError("身份证前17位只能是数字")
            #身份证最后一位数字或X
            id_str_b1 = id_str[-1:]
            if  (not id_str_b1.isdigit()) and id_str_b1!='x' and id_str_b1!='X':
                raise ValidationError("身份证最后一位只能是数字或x")
            id_check(id_str)
        else:
            raise ValidationError("输入的身份证位数不是18位")
    else:
        raise ValidationError("网页编码错误")