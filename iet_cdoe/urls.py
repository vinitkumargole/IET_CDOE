"""iet_cdoe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from main import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contact', views.contact, name="contact"),
    path('faculty', views.faculty, name="faculty"),
    path('programs/<str:pk>', views.programs, name="programs"),
    path('programs/<str:pk>/<str:ic>', views.course, name="course"),
    path('notices', views.notices, name="notices"),
    path('course', views.course, name="course"),
    path('temp', views.temp, name="temp"),
    # path('<str:pk>/',views.prog,name="course")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
