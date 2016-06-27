#-*-coding:UTF-8-*-
from django import forms
from health_card.models import HealthCardInfo

class HealthCardInfoForm(forms.ModelForm):
    name = forms.CharField(max_length=20,help_text='姓名',widget=forms.TextInput(attrs={'class':'weui_input','placeholder':'请输入您的姓名'}))

    class Meta:
        model = HealthCardInfo
        fields = ('name',)