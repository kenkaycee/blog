from django.views.generic import ListView, DetailView, CreateView, UpdateView, DetailView,DeleteView
from .models import Post
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    
class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]
    success_url = reverse_lazy("home")

class BlogUpdateView(UpdateView):    
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]
    success_url = reverse_lazy("home")
    
class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
    
