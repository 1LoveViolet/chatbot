from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('hello/', views.hello, name='hello'),
    # path('msg_data', views.msg_data, name='msg_data'),

]
