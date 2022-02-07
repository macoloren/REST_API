from django.urls import path
from profiles_api import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('usuario/',views.UserAPIView.as_view(), name = 'ussuario_api') 
]


