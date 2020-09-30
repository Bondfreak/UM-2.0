"""Site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from customUser.views import (
    home_screen_view,
    registration_view,
    logout_view,
    login_view,
    custom_user_update_my_data_view,
    custom_user_list_view,
    custom_user_add_view,
    custom_user_update_view,
    custom_user_delete_view,
)


urlpatterns = [
    path('admin/', admin.site.urls),    
    path("", home_screen_view, name="home"),
    path("register/", registration_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path("login/", login_view, name="login"),
    path("user/", custom_user_update_my_data_view, name="customUserUpdateMyData"),
    path("list/", custom_user_list_view, name="customUserList"),
    path("add/", custom_user_add_view, name="customUserAdd"),
    path("update/<pk>/", custom_user_update_view, name="customUserUpdate"),
    path("delete/<pk>/", custom_user_delete_view, name="customUserDelete"),

        # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="password_change_done.html"
        ),
        name="password_change_done",
    ),
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(
            template_name="password_change.html"
        ),
        name="password_change",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password_reset/", auth_views.PasswordResetView.as_view(
            template_name="password_reset_form.html"
        ), name="password_reset"
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
