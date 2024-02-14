from django.urls import path
from todo import views

app_name = 'app'

urlpatterns = [
    path('tasks/', views.TaskItems.as_view(), name='tasks'),
]