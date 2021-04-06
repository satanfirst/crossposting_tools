"""crossposting_tools URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from dj_rest_auth.registration.views import (
    SocialAccountListView, SocialAccountDisconnectView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/registration/', include('dj_rest_auth.registration.urls')),
    path('api/login/', include('dj_rest_auth.urls')),
    path('api/logout/', include('dj_rest_auth.urls'), name='logout'),
    path('api/socialaccounts/', SocialAccountListView.as_view(), name='socialaccount_signup'),
    path('api/socialaccounts/', SocialAccountListView.as_view(), name='socialaccount_connections'),
    path('api/socialaccounts/<int:pk>/disconnect/', SocialAccountDisconnectView.as_view(), name='social_account_disconnect'),

    path('api/facebook/', accounts_views.FacebookLogin.as_view(), name='fb_login'),
    path('api/facebook/connect/', accounts_views.FacebookConnect.as_view(), name='fb_connect'),
    path('api/vk/', accounts_views.VkLogin.as_view(), name='vk_login'),
    path('api/vk/connect/', accounts_views.VkConnect.as_view(), name='vk_connect'),
    path('api/vk/connect/<int:pk>/', accounts_views.VkLogin.as_view(), name='vk_account_connect')
]