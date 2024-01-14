from django.urls import path
from . import views

urlpatterns = [
    path('/home', views.home, name='home'),
    path('', views.home),
    path('create_task', views.create_task, name='create_task'),
    path('update_task/<str:pk>', views.update_task, name='update_task'),
    path('delete_task/<str:pk>', views.delete_task, name='delete_task'),
    path('change_task_completion/<str:pk>', views.change_task_completion, name='change_task_completion'),
    path('reset_task_completion', views.reset_task_completion, name='reset_task_completion')
]