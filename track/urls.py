
from django.urls import path
from track.views import *
from .api import product_list_api, product_detail_api, ProductCraeteAPI, ProductUpdateAPI, ProductDeleteAPI
urlpatterns = [

    path('<int:id>/',mahmoud),
    path('',strin,name='track'),

    #parent
    path('product/list/api', product_list_api),
    path('product/detail/api/<int:product_id>', product_detail_api),
    path('product/create/api/', ProductCraeteAPI.as_view()),
    path('product/update/api/<int:pk>', ProductUpdateAPI.as_view()),
    path('product/delete/api/<int:pk>', ProductDeleteAPI.as_view()),
]