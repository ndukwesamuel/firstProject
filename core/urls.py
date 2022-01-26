"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from HOME.views import ( HomeListView, PostDetail,
         PostCreateView, PostUpdateView, )

from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
)


from Member.views import SignupView, ChangePassword ,password_sucess

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", HomeListView.as_view(), name="home"),
    path("create/", PostCreateView.as_view(), name="create"),
    path("update/<int:pk>", PostUpdateView.as_view(), name="update"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),



    path("password/", ChangePassword.as_view(), name="change_password"),
    path("password_sucess/", password_sucess, name="password_sucess"),





    

    path("<int:pk>", PostDetail.as_view(), name="Detail")

    

]
