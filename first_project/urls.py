"""
URL configuration for first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from string import Template
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from book_store.views import SignUpView, profile_view
from first_project import settings
from django.conf.urls.static import static
# from django_app.views import BookListCreateAPIView




urlpatterns = [
    path('admin/', admin.site.urls),
    path("books/", include("book_store.urls")),
    path('api/', include('django_app.urls')),
    # Includes all auth URLs (login, logout, password reset, etc.)
    path('accounts/', include('django.contrib.auth.urls')),
    # A protected profile page view
    path('accounts/profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
    # A protected profile page view
    # path('accounts/profile/', profile_view, name='profile'),

    path('signup/', SignUpView.as_view(), name='signup'),
]

# serve static files locally during development
# for development only
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

