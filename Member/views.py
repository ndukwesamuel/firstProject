from django.shortcuts import render,reverse
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms  import PasswordChangeForm
from django.urls import reverse_lazy


# Create your views here.

from django.views import generic
from .forms import CustomUserCreationForm

# from Member.forms import CustomUserCreationForm
class SignupView(generic.CreateView):
    template_name = "registration/Signup.html"
    form_class = CustomUserCreationForm
    def get_success_url(self):
        return reverse("login")

class ChangePassword(auth_views.PasswordChangeView):
    template_name = "registration/change-password.html"
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_sucess')
    


def password_sucess(request):

    return render(request, "registration/password_success.html" )



    

