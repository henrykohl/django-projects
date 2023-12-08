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
from pages.views import home_view, contact_view, about_view, social_view # 法2

from products.views import (
    product_detail_view,  # 21
    product_create_view,  # 23
    render_initial_data,  # 28
    dynamic_lookup_view,  # 29
    product_delete_view,  # 31
    product_list_view,    # 32
)

# from products.views import (
#     product_detail_view,
#     product_delete_view,  # 31
#     product_create_view,
#     product_list_view,    # 32
#     # render_initial_data,  # 28
#     # dynamic_lookup_view,  # 29/34 
#     product_update_view,  # 35 
# )

# urlpatterns = [
#     # path('', views.home_view, name='home'), # 法1
#     path('', home_view, name='home'),         # 法2
#     path('home/', home_view, name='home'),
#     path('contact/', contact_view),
#     # path('create/', product_create_view), 

#     path('about/', about_view),
#     path('admin/', admin.site.urls),
# ]

"""節21~節34"""
urlpatterns = [
    path('', home_view, name='home'),         
    path('home/', home_view, name='home'),
    path('contact/', contact_view),
    # path('create/', product_create_view),  # 節23
    path('create/', render_initial_data),   # 節28
    
    path('products/<int:my_id>/delete/',product_delete_view, name='product-delete'), # 節31
    path('products/',product_list_view, name='product_list'), # 節32/33
    # path('products/<int:my_id>/',dynamic_lookup_view, name='product'), # 節29
    path('products/<int:my_id>/',dynamic_lookup_view, name='product-detail'), # 節34

    path('product/', product_detail_view),  # 節21/22/
    path('about/', about_view),
    path('admin/', admin.site.urls),

]

