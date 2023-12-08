from django.forms import ModelForm
from .models import Room, User 
# from django.contrib.auth.models import User # (removed)

from django.contrib.auth.forms import UserCreationForm # 新增

class MyUserCreationForm(UserCreationForm): # 新增
    class Meta:
        model = User
        fields = ['name','username', 'email', 'password1', 'password2']

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants'] 

class RoomFormM(RoomForm): # 自訂
    class Meta:
        model = Room
        fields = ['name','description']

class UserForm(ModelForm): # 
    class Meta:
        model = User
        # fields = ['username','email']
        fields = ['avatar', 'name', 'username','email', 'bio'] 
