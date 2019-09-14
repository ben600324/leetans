from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Recipe, Carousel, Contact


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all().values('title', 'content', 'date_posted', 'author')
        return Response({"posts": posts})

class PostListView(ListView):
    # model = Post
    # template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    # context_object_name = 'posts'
    # ordering = ['-date_posted']
    # paginate_by = 5
    model = Post
    template_name = 'blog/home.html' 
    
    def get_context_data(self, *args, **kwargs):
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context['posts_one'] = Post.objects.all()[0:1]
        context['posts_two'] = Post.objects.all()[0:2]
        context['latest_recipes'] = Recipe.objects.all().order_by('-id')[:6]
        context['top_recipes'] = Recipe.objects.all().order_by('-id')[:5]
        context['most_liked_recipes'] = Recipe.objects.all().order_by('id')[:5]
        context['carousels'] = Carousel.objects.all()
        return context

class RecipeListView(ListView):
    model = Recipe
    template_name = 'blog/recipes.html'   # <app>/<model>_<viewtype>.html
    context_object_name = 'all_recipes'
    ordering = ['-date_posted']
    paginate_by = 3

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


class ContactCreateView(CreateView):
    model = Contact
    template_name = 'blog/contact.html'   # <app>/<model>_<viewtype>.html
    fields = ['name', 'email', 'subject', 'message']
