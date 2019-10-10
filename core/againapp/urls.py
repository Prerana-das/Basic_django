from django.urls import path

from .views import test_index_func,test_index_func2
#view func import and .views means immediate view file /folder er mdder file

urlpatterns = [
    path('',test_index_func,name = 'Test index Function'), ##for black use only one space
    path('another/', test_index_func2, name='Test index Function 2')
]