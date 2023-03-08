from django.urls import path

from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('register/',views.registerPage, name='register'),
    path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutUser, name='logout'),
    path('user/', views.userPage, name="user_page"),
    path('update_user/', views.updateUser, name="update_user"),

    path('', views.index, name='home'),
    path('produkty', views.produkty, name='produkty'),
    path('klient/<str:pk>', views.klient, name='klient'),
    path('produkt/<str:pk>', views.produkt, name='produkt'),
    path('create_produkt/<str:pk>', views.createProdukt, name='create_produkt'),
    path('create_klient', views.createKlient, name='create_klient'),
    path('update_klient/<str:pk>', views.updateKlient, name='update_klient'),
    path('update_produkt/<str:pk>', views.updateProdukt, name='update_produkt'),
    path('delete_klient/<str:pk>', views.deleteKlient, name='delete_klient'),
    path('delete_produkt/<str:pk>', views.deleteProdukt, name='delete_produkt'),
   
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
