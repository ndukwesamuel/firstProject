from django.shortcuts import render

# Create your views here.
from django.views.generic import (TemplateView, ListView,
                                     DetailView, CreateView,
                                      UpdateView)

from HOME.models import Post

from HOME.forms import Post_Form, Edit_Post_Form



# class HomeView(TemplateView):
#     template_name = "base.html"



class HomeListView(ListView):
    model = Post
    template_name = "index.html"


class PostDetail(DetailView):
    model = Post
    template_name = "details.html"

class PostCreateView(CreateView):
    model = Post
    template_name = "create.html"
    # fields = '__all__'
    form_class = Post_Form


class PostUpdateView(UpdateView):
    model = Post
    template_name = "Update.html"
    # fields = '__all__'
    form_class = Edit_Post_Form









