from sys import prefix
from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



router_user=DefaultRouter()

router_user.register(
    prefix='users', basename='users', viewset=views.UserApiViewSet
)

urlpatterns =[
    path('auth/me/', views.UserView.as_view()),
    path('auth/login/',TokenObtainPairView.as_view(), name='token_obtain_pair')
]