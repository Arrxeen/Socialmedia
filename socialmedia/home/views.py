from typing import Any
from django.shortcuts import render, redirect
from home.models import Category, Post
from django.views.generic import CreateView, DetailView
from home.forms import PostForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'home/index.html', context = {'posts': posts, 'categories': categories})
# def index2(request):
#     return render(request, 'home/mk-new-post.html')

class CreatePostView(CreateView):
    template_name = 'home/mk-new-post.html'
    form_class = PostForm

    def form_valid(self,form):
        data = form.data
        post = Post(name = data.get('name'), content = data.get('content'), link = data.get('link'), category_id = data.get('category'))
        # post.author = User.objects.get(pk=1)
        post.author = self.request.user
        post.save()
        return redirect('home')
    def get_context_data(self, **kwargs: Any) -> dict:
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    
class CategoryView(DetailView):
    model = Category
    template_name = "home/category.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["posts"] = Post.objects.filter(category=kwargs["object"])
        return context
