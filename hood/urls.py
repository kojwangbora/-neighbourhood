from xml.etree.ElementInclude import include
from django.urls import path, re_path, include
from . import views

urlpatterns=[
    path('', views.index, name= 'index'),
    path('register/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('all-hoods/', views.hoods, name='hood')
]