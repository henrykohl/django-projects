from django.urls import path
from . import views

urlpatterns = [
  path('', views.predictor, name='predictor'),
  # path('result', views.formInfo, name = 'result') # 用在方法一，方法二用不到
]