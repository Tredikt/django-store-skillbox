from django.contrib.auth.views import LoginView
from django.urls import path


from .views import (
    HelloView,
    get_cookie_view,
    set_cookie_view,
    set_session_view,
    get_session_view,
    MyLogoutView,
    AboutMeView,
    UpdateProfileView,
    UpdateUserView,
    RegisterView,
    FooBarView,
    UsersListView,
    UserDetailsView,
)

app_name = "myauth"

urlpatterns = [
    # path("login/", login_view, name="login"),
    path(
        "login/",
        LoginView.as_view(
            template_name="myauth/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path("hello/", HelloView.as_view(), name="hello"),
    # path("logout/", logout_view, name="logout"),
    path("logout/", MyLogoutView.as_view(), name="logout"),
    path("about-me/", AboutMeView.as_view(), name="about-me"),
    path("about-me/<int:pk>/update-profile/", UpdateProfileView.as_view(), name="update-profile"),
    path("about-me/<int:pk>/update-user/", UpdateUserView.as_view(), name="update-user"),
    path("register/", RegisterView.as_view(), name="register"),

    path("cookie/get/", get_cookie_view, name="cookie-get"),
    path("cookie/set/", set_cookie_view, name="cookie-set"),

    path("session/set/", set_session_view, name="session-set"),
    path("session/get/", get_session_view, name="session-get"),

    path("foo-bar/", FooBarView.as_view(), name="foo-bar"),
    path("users-list/", UsersListView.as_view(), name="users-list"),
    path("user-details/<int:pk>/", UserDetailsView.as_view(), name="user-details"),

]
