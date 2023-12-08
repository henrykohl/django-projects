from django.urls import path

from products.views import (
        product_detail_view,  # 21/22
        product_delete_view,  # 31
        product_create_view,  # 23(27)/24/25
        product_list_view,    # 32
        product_update_view,  # 35 
    )

app_name="products" # 修正後
# 35
urlpatterns = [
	# 修正前
    # path('products/',product_list_view, name='product-list'),                        # 32
    # path('products/create/', product_create_view, name='product-list'),              # 35
    # path('products/<int:my_id>/',product_detail_view, name='product-detail'),        # 35 
    # path('products/<int:my_id>/update/',product_update_view, name='product-update'), # 35
    # path('products/<int:my_id>/delete/',product_delete_view, name='product-delete'), # 31
	
    # 修正後
	path('',product_list_view, name='product-list'),                        # 32
    path('create/', product_create_view, name='product-list'),              # 35
    path('<int:my_id>/',product_detail_view, name='product-detail'),        # 35 
    path('<int:my_id>/update/',product_update_view, name='product-update'), # 35
    path('<int:my_id>/delete/',product_delete_view, name='product-delete'), # 31
]