from django.urls import path
from . import views

urlpatterns = [
    path('api', views.get_info , name = 'get_info'),
    #path('api/', views.get_info , name = 'get_info'),

    path('', views.home , name = 'home' ),
]
