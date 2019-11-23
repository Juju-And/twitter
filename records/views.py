from django.shortcuts import render
from django.views import View
from records.models import Tweet
from records.forms import AddTweetForm
from django.views.generic import FormView, UpdateView


class MainView(View):
    def get(self, request):
        tweets = Tweet.objects.all()
        return render(request, 'index.html', {"tweets": tweets})


class AddTweetView(FormView):
    template_name = "add_tweet.html"
    form_class = AddTweetForm
    success_url = "/"
