from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [
    # Welcoming page
    path('', views.index, name='index'),
    # Home page
    path('home/', views.home, name='home'),
    # New post page
    path('new_post/', views.new_post, name='new_post'),
    # Edit post page
    path('edit_post/<int:blogpost_id>/', views.edit_post, name='edit_post')
]
