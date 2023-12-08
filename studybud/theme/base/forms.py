from django.forms import ModelForm
from django.forms import ValidationError # 自加
from .models import Room
from django.contrib.auth.models import User # 新增

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants'] 
    
    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     print(">>>>>XO")
    #     if self.instance.id:
    #         if Room.objects.filter(name=name).exclude(id=self.instance.id):
    #             raise ValidationError(
    #                         'Menu with this title already exists.')
    #         else:
    #             if Room.objects.filter(name=name):
    #                 raise ValidationError(
    #                         'Menu with this subject already exists.')
    #         return name

class RoomFormM(RoomForm): # 自訂
    class Meta:
        model = Room
        fields = ['name','description']

class UserForm(ModelForm): # 新增
    class Meta:
        model = User
        fields = ['username','email']
