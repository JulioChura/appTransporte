from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserList, UserDetail, UserRegister, ClienteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='cliente')

urlpatterns = [
    path('usuarios/', UserList.as_view(), name="user_list"),
    path('usuarios/<int:pk>/', UserDetail.as_view(), name="user_detail"),
    path('usuarios/registro/', UserRegister.as_view(), name="user_register"),
    path('usuarios/login/', obtain_auth_token, name="api_token_auth"),
    # crud para las demas tablas
    
    path('', include(router.urls)),
]