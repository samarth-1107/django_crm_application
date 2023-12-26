from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    # CRUD
    path('dashboard', views.dashboard, name="dashboard"),
    path('create-record', views.create_record, name="create-record"),

]