import csv
import io
import datetime

from django.shortcuts import render, redirect
from service.models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .forms import PostForm, CommentForm, UserRegisterForm, MessageForm


def index(request):
    return render(request, 'index.html')


def about(request):
    form = MessageForm
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get("title")
            body = form.cleaned_data.get("body")
            try:
                send_mail(subject, body, settings.EMAIL_HOST_USER, ["example@mail.ru"], fail_silently=False)
                form.save()
                messages.success(request, f"Message sent successfully")
            except Exception as err:
                print(str(err))
            return redirect('index')
    return render(request, 'about.html', {"form": form})


class PostsView(ListView):
    model = Post
    template_name = "index.html"
    ordering = ['-created_at']


class DetailPostView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Post
    template_name = "detail_post.html"


# class CreatePostView(LoginRequiredMixin, CreateView):
#    login_url = 'login'
#    model = Post
#    template_name = "create_post.html"
#    form_class = PostForm


@login_required
def create_post(request):
    form = PostForm
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get("title")
            # id = form.cleaned_data.get("pk")
            if title != "POST":
                messages.error(request, f"Something went wrong")
                return redirect('index')
            messages.success(request, f"Post {title} was created successfully")
            return redirect('index')
    return render(request, "create_post.html", {"form": form})


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


class Register(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    success_message = "%(username)s was created successfully"
    template_name = "register.html"
    success_url = reverse_lazy('login')


def upload(request):
    context = {}
    if request.method == "POST":
        uploaded_file = request.FILES['file']
        file = FileSystemStorage()
        name = file.save(uploaded_file.name, uploaded_file)
        messages.success(request, f"Upload file successfully")
        context['url'] = file.url(name)
    return render(request, 'upload.html', context)


def download(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(["Title", "Description", "Created_at"])

    for row in Post.objects.all().values_list('title', 'description', 'created_at'):
        writer.writerow(row)
    filename = str(datetime.datetime.now())
    response["Content-Disposition"] = f"attachment; filename={filename} posts.csv"
    return response
