"""repo_name URL Configuration

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
from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from users import views as user_views
from reddit import views as reddit_views
urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('register/', user_views.register, name="register"),
    path('login/', user_views.user_login, name="login"),
    path('logout/', user_views.user_logout, name="logout"),
    path('user/<username>/', user_views.user_profile, name="user_profile"),
    path('profile/edit/', user_views.edit_profile, name="edit_profile"),
    path('', reddit_views.frontpage, name="frontpage"),
    path('comments/<int:thread_id>/', reddit_views.comments, name="thread"),
    path('submit/', reddit_views.submit, name="submit"),
    path('post/comment/', reddit_views.post_comment, name="post_comment"),
    path('vote/', reddit_views.vote, name="vote"),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
