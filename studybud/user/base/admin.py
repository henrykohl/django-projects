from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Message, User # 新增 User

admin.site.register(User) # 新增 
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)