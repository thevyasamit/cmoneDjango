"""django_reddit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.urls import include,path
import debug_toolbar
from . import views

urlpatterns = [
    path('', views.frontpage, name="frontpage"),
    path('comments/(<thread_id>[0-9]+)', views.comments, name="thread"),
    path('submit/', views.submit, name="submit"),
    path('post/comment/', views.post_comment, name="post_comment"),
    path('vote/', views.vote, name="vote"),
    path('__debug__/', include(debug_toolbar.urls, namespace='djdt')),

]

