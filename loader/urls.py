from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('detail_hor/<int:page>', views.detail_1, name='detail_hor'),
    path('detail_ver/<int:page>', views.detail_2, name='detail_ver'),
]