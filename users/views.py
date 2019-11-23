from django.shortcuts import render, redirect
from django.views.generic import FormView
from users.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            messages.error(self.request, "User or password invalid!")
            return super().form_invalid(form)

    success_url = '/'


@login_required(login_url="/login")
def logoutUser(request):
    logout(request)
    return redirect("/")


class CreateUser(FormView):
    pass
