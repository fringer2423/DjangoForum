from django.shortcuts import render, redirect
from service.models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, CommentForm, UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


def index(request):
    return render(request, 'index.html')


@login_required
@permission_required('service.view_post')
def about(request):
    return render(request, 'about.html')


class PostsView(ListView):
    model = Post
    template_name = "index.html"
    ordering = ['-created_at']


class DetailPostView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Post
    template_name = "detail_post.html"


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Post
    template_name = "create_post.html"
    form_class = PostForm


class UpdatePostView(PermissionRequiredMixin, UpdateView):
    permission_required = 'service.change_post'
    login_url = 'login'
    model = Post
    template_name = "update_post.html"
    form_class = PostForm


class DeletePostView(PermissionRequiredMixin, DeleteView):
    permission_required = 'delete_post'
    login_url = 'login'
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('index')


class AddComment(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Comment
    template_name = "add_comment.html"
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


class Register(CreateView):
    form_class = UserRegisterForm
    template_name = "register.html"
    success_url = reverse_lazy('login')
