from django.urls import path, include
from service import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register', views.Register.as_view(), name='register'),
    path('', views.PostsView.as_view(), name='index'),
    path('about', views.about, name='about'),
    path('post/<int:pk>', views.DetailPostView.as_view(), name='detail_post'),
    path('create_post', views.CreatePostView.as_view(), name='create_post'),
    path('update_post/<int:pk>', views.UpdatePostView.as_view(), name='update_post'),
    path('delete_post/<int:pk>', views.DeletePostView.as_view(), name='delete_post'),
    path('post/<int:pk>/add_comment', views.AddComment.as_view(), name='add_comment'),
]
