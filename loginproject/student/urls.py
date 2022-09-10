from django.urls import path
from . import views
urlpatterns =[
    path( '' , views.home),
    path( 'registerfunction' , views.registerfunction),
    path( 'loginfunction' , views.loginfunction),
    path( 'login' , views.login),
    path( 'register' , views.register),
    path( 'display' , views.display),
    path( 'edit/<int:id>' , views.editfunction, name='edit'),
    path( 'delete/<int:id>' , views.deletefunction, name='delete'),
]