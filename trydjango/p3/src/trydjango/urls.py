"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # 35 新加 include

# from pages import views          # 法1
from pages.views import home_view, contact_view, about_view, social_view  # 法2

# from products.views import product_detail_view # 21/22, product_create_view # 23(27)/24/25/, render_initial_data # 28

"""from 節35"""
from products.views import (
    product_detail_view,  # 21/22
    product_delete_view,  # 31
    product_create_view,  # 23(27)/24/25
    product_list_view,    # 32
    # render_initial_data,  # 28
    # dynamic_lookup_view,  # 29/34 
    product_update_view,  # 35 
)

"""before 節35"""
# urlpatterns = [
#     # path('', views.home_view, name='home'), # 法一
#     path('', home_view, name='home'),         # 法二
#     path('home/', home_view, name='home'),
#     path('contact/', contact_view),
#     # path('create/', product_create_view), 
#     path('create/', render_initial_data),   # 節28
    
#     path('products/<int:my_id>/delete/',product_delete_view, name='product-delete'), # 節31
#     path('products/',product_list_view, name='product-list'), # 節32
#     # path('products/<int:my_id>/',dynamic_lookup_view, name='product'), # 節29
#     path('products/<int:my_id>/',dynamic_lookup_view, name='product-detail'), # 節34

#     path('product/', product_detail_view),  # 節21/22/
#     path('about/', about_view),
#     path('admin/', admin.site.urls),
# ]

"""from 節35"""
urlpatterns = [
    path('blog/', include('blog.urls')),            # 36
    path('products/', include('products.urls')),    # 35
    path('courses/', include('courses.urls')),      # 40

    # path('products/',product_list_view, name='product-list'),                        # 32
    # path('products/create/', product_create_view, name='product-list'),              # 35
    # path('products/<int:my_id>/',product_detail_view, name='product-detail'),        # 35 
    # path('products/<int:my_id>/update/',product_update_view, name='product-update'), # 35
    # path('products/<int:my_id>/delete/',product_delete_view, name='product-delete'), # 31
    
    path('', home_view, name='home'),
    path('about/', about_view, name='product-detail'),             # 35 (name='product-detail'的方式不好，但不會引起錯誤)
    # path('about/<int:my_id>/', about_view, name='product-detail'),    # 35 (展示錯誤範例, name='about-detail'就正確了)
    path('contact/', contact_view),
    path('admin/', admin.site.urls),
]