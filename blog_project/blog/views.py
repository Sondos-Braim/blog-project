from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Post
# Create your views here.
class blog_view(ListView):
    template_name='home.html'
    model= Post

class details_view(DetailView):
    template_name='details.html'
    model=Post