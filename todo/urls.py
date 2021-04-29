from django.urls import path
from todo import views

app_name = 'todo'

urlpatterns = [
    path('create/', views.TodoCreate.as_view(), name='create'),
    path('', views.TodoList.as_view(), name='list'),
    path('completed/', views.TodoCompletedList.as_view(), name='complete_list'),
    path('<int:pk>/', views.TodoDetail.as_view(), name='detail'),
    path('<int:pk>/delete', views.TodoDelete.as_view(), name='delete'),
    path('<int:pk>/edit/', views.TodoEdit.as_view(), name='edit'),
    path('<int:pk>/complete/', views.TodoComplete.as_view(), name='complete'),
]
