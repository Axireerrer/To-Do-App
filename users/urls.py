from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutUser, name='logout'),
]