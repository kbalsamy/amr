from django.urls import path, include
from .views import mainView, downloadView

app_name = 'dashboard'

urlpatterns = [path('', mainView, name='home'),
               path('download', downloadView, name='dbconnect'), ]
