from django.shortcuts import render
from django.views import View
from records.models import Tweet
from records.forms import TweetForm
from django.views.generic import FormView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class MainView(LoginRequiredMixin, View):
    login_url = '/login'

    def get(self, request):
        tweets = Tweet.objects.all()
        return render(request, 'index.html', {"tweets": tweets})


class AddTweetView(LoginRequiredMixin, CreateView):
    login_url = '/login'
    template_name = "add_tweet.html"
    form_class = TweetForm
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TweetView(View):
    def get(self, request, tweet_id):
        current_tweet = Tweet.objects.get(id=tweet_id)
        return render(request, 'tweet_info.html', {"current_tweet": current_tweet})
