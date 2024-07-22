from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserList, UserDetail, UserRegister, ClienteCreateView, LoginView, RutaListView, RegisterTripView
from rest_framework.routers import DefaultRouter

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
]