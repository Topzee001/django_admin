from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import approve_student_view
from django.contrib.auth import views as auth_views



urlpatterns = [
    path("", views.intro, name="intro"),
    path("hello/", views.HelloView.as_view(), name="hello_view"),
    path("detail/", views.BookDetailView.as_view(), name="about"),
# practice exercise for views and url section
    path("task/", views.task, name='task'),
    path("greeting/", views.greeting.as_view(), name="greeting"),
    # dynamic url with params (e.g /book/3/)
    path("book/<int:id>/", views.BookDetailView.as_view(), name='book_detail'),
    path('approve/<int:student_id>/', approve_student_view, name='approve_student'),
    path('students/<int:student_id>/approve/', approve_student_view, name='approve_student'),
   

]
