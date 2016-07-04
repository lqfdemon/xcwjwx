#-*-coding:UTF-8-*-
from django import forms
from health_card.models import HealthCardInfo,EducationInfo,NationInfo,UnitInfo,SalaryBankInfo,HandingBankInfo
from health_card.form_check import validate_id_num


class HealthCardInfoForm(forms.ModelForm):
    name = forms.CharField(
        max_length=20,
        label='姓名：',
        widget=forms.TextInput(attrs={'class':'weui_input','placeholder':'请输入您的姓名'}),
    )
    id_num=forms.CharField(
        validators=[validate_id_num],
        label='身份证号：',
        widget=forms.TextInput(attrs={'class': 'weui_input', 'placeholder': '请输入您的身份证号码'}),
    )
    nation =forms.ModelChoiceField(
        initial='请选择',
        widget=forms.Select(attrs={'class': 'weui_select'}),
        queryset=NationInfo.objects.all(),
        required=True,
        label='民族：',
        error_messages={'required': '必选项'},
    )
    unit_name =forms.ModelChoiceField(
        initial='请选择',
        widget=forms.Select(attrs={'class': 'weui_select'}),
        queryset=UnitInfo.objects.all(),
        required=True,
        label='经办单位：',
        error_messages={'required': '必选项'},
    )
    education_back = forms.ModelChoiceField(
        initial='请选择',
        widget=forms.Select(attrs={'class': 'weui_select'}),
        queryset=EducationInfo.objects.all(),
        required=True,
        label= '文化程度：',
        error_messages={'required':'必选项'},
    )
    book_address = forms.CharField(
        max_length=100,
        label='户籍地址：',
        widget=forms.TextInput(attrs={'class':'weui_input','placeholder':'请输入您的户籍地址'}),
    )
    address = forms.CharField(
        max_length=100,
        label='现住址：',
        widget=forms.TextInput(attrs={'class':'weui_input','placeholder':'请输入您的现住址'}),
    )
    tel=forms.IntegerField(
        label='电话号码：',
        widget=forms.TextInput(attrs={'class': 'weui_input', 'placeholder': '请输入您的电话号码'}),
    )
    nonghe_id=forms.IntegerField(
        label='新农合号：',
        widget=forms.TextInput(attrs={'class': 'weui_input', 'placeholder': '请输入您的电话号码'}),
    )
    shebao_id=forms.IntegerField(
        label='社保卡号：',
        widget=forms.TextInput(attrs={'class': 'weui_input', 'placeholder': '请输入您的电话号码'}),
    )
    salary_bank =forms.ModelChoiceField(
        initial='请选择',
        widget=forms.Select(attrs={'class':'weui_select'}),
        queryset=SalaryBankInfo.objects.all(),
        required=True,
        label='工资卡发放银行：',
        error_messages={'required': '必选项'},
    )
    handing_bank =forms.ModelChoiceField(
        initial='请选择',
        widget=forms.Select(attrs={'class': 'weui_select'}),
        queryset=HandingBankInfo.objects.all(),
        required=True,
        label='健康卡办理银行：',
        error_messages={'required': '必选项'},
    )
    class Meta:
        model = HealthCardInfo
        fields = ('name',)