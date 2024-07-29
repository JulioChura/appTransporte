from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserList, UserDetail, UserRegister, ClienteCreateView, LoginView, RutaListView, RegisterTripView, HistoryTripView
from rest_framework.routers import DefaultRouter
from .views import SendPDFView

from .views import *
urlpatterns = [
    path('usuarios/', UserList.as_view(), name="user_list"),
    path('usuarios/<int:pk>/', UserDetail.as_view(), name="user_detail"),
    path('usuarios/registro/', UserRegister.as_view(), name="user_register"),
    path('usuarios/login/', obtain_auth_token, name="api_token_auth"),
    # crud para las demas tablas
    path('register/', ClienteCreateView.as_view(), name="crear"),
    path('login/', LoginView.as_view(), name='login'),
    path('rutas/', RutaListView.as_view(), name='ruta_list'),
    path('registrar_viaje/', RegisterTripView.as_view(), name='register_trip'),
    path('clientes/<int:cliente_id>/historial/', HistoryTripView.as_view(), name='cliente-historial-viajes'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # debe ir a la rama principal este cambio
    path('create_preference/<int:precio>/<str:ruta>/<int:ruta_id>/<int:user_id>/', create_preference, name='create_preference'),
    #path('create_preference/<int:precio>/<int:ruta_id>/', create_preference, name='create_preference'),
    #path('payment_notification/', PaymentNotificationView.as_view(), name='payment_notification'),
    path('registrar_viaje/', RegisterTripView.as_view(), name='register_trip'),
    path('send-email/', SendPDFView.as_view(), name='send_email'),
]