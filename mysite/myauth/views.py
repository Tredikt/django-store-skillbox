from random import random

from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView
from django.urls import reverse
from django.utils.translation import gettext_lazy as _, ngettext
from django.views.decorators.cache import cache_page

from .models import Profile
from .forms import ProfileUpdateForm, UserUpdateForm


class HelloView(View):
    welcome_message = _("welcome hello word!")

    def get(self, request: HttpRequest) -> HttpResponse:
        items_str = request.GET.get("items") or 0
        items = int(items_str)
        product_line = ngettext(
            "one product",
            "{count} products",
            items
        )
        product_line = product_line.format(count=items)
        return HttpResponse(
            f"<h1>{self.welcome_message}</h1>"
            f"\n<h2>{product_line}</h2>"
        )


class AboutMeView(TemplateView):
    template_name = "myauth/about-me.html"


class UpdateProfileView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name_suffix = "_update_form"


    def get_success_url(self):
        return reverse("myauth:about-me")


    def form_valid(self, form):
        response = super(UpdateProfileView, self).form_valid(form)
        return response


class UpdateUserView(UpdateView, UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.is_staff or user == Profile.user
    model = User
    form_class = UserUpdateForm
    template_name = "myauth/user_update_form.html"


    def get_success_url(self):
        return reverse("myauth:about-me")


    def form_valid(self, form):
        response = super(UpdateUserView, self).form_valid(form)
        return response




class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "myauth/register.html"
    success_url = reverse_lazy("myauth:about-me")

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)
        return response


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("myauth:login")


@user_passes_test(lambda u: u.is_superuser)
def set_cookie_view(request: HttpRequest) -> HttpResponse:
    response = HttpResponse("Cookie set")
    response.set_cookie("fizz", "buzz", max_age=3600)
    return response


@cache_page(60 * 2)
def get_cookie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get("fizz", "default value")
    return HttpResponse(f"Cookie value: {value!r} + {random()}")


@permission_required("myauth.view_profile", raise_exception=True)
def set_session_view(request: HttpRequest) -> HttpResponse:
    request.session["foobar"] = "spameggs"
    return HttpResponse("Session set!")


@login_required
def get_session_view(request: HttpRequest) -> HttpResponse:
    value = request.session.get("foobar", "default")
    return HttpResponse(f"Session value: {value!r}")


class FooBarView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        return JsonResponse({"foo": "bar", "spam": "eggs"})


class UsersListView(ListView):
    template_name = "myauth/users-list.html"
    context_object_name = "users"
    queryset = User.objects.all()


class UserDetailsView(DetailView):
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff is False:
            profile = self.get_object()
            if self.request.user.profile.pk == profile.pk:
                return redirect(reverse("myauth:about-me"))
        return super().get(request, *args, **kwargs)

    template_name = "myauth/user-detail.html"
    context_object_name = "profile"
    model = Profile

