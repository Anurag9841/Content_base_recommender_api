from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('data_retrival/<slug:table_name>',views.data_retrival,name = 'data_retrival'),
    path('data_show/<str:table_name>',views.data_show,name = 'data_show'),
    path('preprocess_data/<str:table_name>',views.preprocess_data,name = 'preprocess_data'),
    path('preprocess_data_show/<str:table_name>',views.data_show_preprocessed,name = 'preprocess_show')
]