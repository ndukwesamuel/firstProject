from django.shortcuts import render,reverse

# Create your views here.

from django.views import generic
from .forms import CustomUserCreationForm



class SignupView(generic.CreateView):
    template_name = "registration/Signup.html"
    form_class = CustomUserCreationForm


    def get_success_url(self):
        return reverse("login")
    

