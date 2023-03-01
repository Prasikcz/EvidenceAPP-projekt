from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.registerPage, name='register'),
    path('login/',views.loginPage, name='login'),


    path('', views.index, name='home'),
    path('klient/<str:pk>', views.klient, name='klient'),
    path('produkt/<str:pk>', views.produkt, name='produkt'),
    path('create_produkt/<str:pk>', views.createProdukt, name='create_produkt'),
    path('create_klient', views.createKlient, name='create_klient'),
    path('update_klient/<str:pk>', views.updateKlient, name='update_klient'),
    path('update_produkt/<str:pk>', views.updateProdukt, name='update_produkt'),
    path('delete_klient/<str:pk>', views.deleteKlient, name='delete_klient'),
    path('delete_produkt/<str:pk>', views.deleteProdukt, name='delete_produkt'),
   

]
