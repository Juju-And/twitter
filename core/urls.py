"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from records.views import (MainView,
                           AddTweetView,
                           TweetView,
                           UsersTweetsView
                           )
from users.views import (LoginView,
                         logoutUser,
                         CreateUserView)
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', MainView.as_view(), name="index"),
    url(r'^add_tweet', AddTweetView.as_view()),
    url(r'^login', LoginView.as_view()),
    url(r'^logout', logoutUser),
    url(r'^create_user', CreateUserView.as_view()),
    url(r'^tweet/(?P<tweet_id>(\d)+)', TweetView.as_view(), name="tweet"),
    url(r'^users_tweets', UsersTweetsView.as_view()),

]
