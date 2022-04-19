from xml.etree.ElementInclude import include
from django.urls import path, re_path, include
from . import views

urlpatterns=[
    path('', views.index, name= 'index'),
    path('register/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('all-hoods/', views.hoods, name='hood'),
    path('profile/<username>', views.profile, name='profile'),

    path('profile/<username>/edit/', views.edit_profile, name='edit-profile'),
    path('join_hood/<id>', views.join_hood, name='join_hood'),
    path('new-hood/', views.create_hood, name='new-hood'),
]