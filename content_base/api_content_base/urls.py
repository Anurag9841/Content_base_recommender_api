from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('data_retrival/<slug:table_name>',views.data_retrival,name = 'data_retrival'),
]