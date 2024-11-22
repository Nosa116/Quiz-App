from django.urls import re_path
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('login', views.login),
    path('signup', views.signup),
    path('test_token', views.test_token),
    path('admin/', admin.site.urls),
    path('question/', views.quiz_questions),

]
