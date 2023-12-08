from django.urls import path # (40)
from .views import (
    CourseView,          # 40
    CourseListView,      # 42
    MyListView,          # 42
    CourseCreateView,    # 43
    CourseUpdateView,    # 45
    CourseDeleteView,    # 46
    my_fbv               # 40
)

app_name = 'courses' # 40
urlpatterns = [
    # path('', CourseView.as_view(), name='courses-list'), # 40
    # path('', CourseView.as_view(template_name='contact.html'), name='courses-list'), # 40
    path('', CourseListView.as_view(), name='courses-list'),   # 42
    # path('', MyListView.as_view(), name='courses-list'),      # 42
    # path('', my_fbv, name='courses-list'), # 40

    path('create/', CourseCreateView.as_view(), name='courses-create'), # 43
    path('<int:id>/', CourseView.as_view(), name='courses-detail'), # 41
    path('<int:id>/update/', CourseUpdateView.as_view(), name='courses-update'), # 45
    path('<int:id>/delete/', CourseDeleteView.as_view(), name='courses-delete'), # 46
]