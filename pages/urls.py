from django.urls import path

from .views import HomePage, CreateUser

urlpatterns = [
    path('view/', HomePage.as_view(), name='home'),
    path('createuser/', CreateUser.as_view(), name = 'createUser')
]