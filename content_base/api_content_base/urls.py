from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('data_retrival/<slug:table_name>',views.data_retrival,name = 'data_retrival'),#path to store data in database
    path('data_show/<str:table_name>',views.data_show,name = 'data_show'),#path to show data stored in database
    path('preprocess_data/<str:table_name>',views.preprocess_data,name = 'preprocess_data'),#path to preprocess data
    path('preprocess_data_show/<str:table_name>',views.data_show_preprocessed,name = 'preprocess_show'),#path to show preprocess data
    path('cosine_indices',views.cosine_sim_indices_maker,name = 'cosine_indices'),#path to make coisne similarity and indices
    path('cosine_recommendation/<int:course_id>',views.content_reco,name = 'content_base'),#path to show recommendation
    path('course_list',views.ui_recommendation,name = 'ui-reco')
]