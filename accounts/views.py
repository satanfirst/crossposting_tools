from django.shortcuts import render

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView

from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from dj_rest_auth.social_serializers import TwitterLoginSerializer

from dj_rest_auth.registration.views import SocialConnectView
from dj_rest_auth.social_serializers import TwitterConnectSerializer

from allauth.socialaccount.providers.vk.views import VKOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.social_serializers import SocialConnectMixin
from .serializers import VKOAuth2Serializer


class VKOAuth2ConnectSerializer(SocialConnectMixin, VKOAuth2Serializer):
    pass


class VkLogin(SocialLoginView):
    adapter_class = VKOAuth2Adapter
    serializer_class = VKOAuth2Serializer
    callback_url = 'http://crossposting.ru/api/socialaccounts/'
    client_class = OAuth2Client


class VkConnect(SocialConnectView):
    adapter_class = VKOAuth2Adapter
    serializer_class = VKOAuth2ConnectSerializer


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class FacebookConnect(SocialConnectView):
    adapter_class = FacebookOAuth2Adapter


class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter


class TwitterConnect(SocialConnectView):
    serializer_class = TwitterConnectSerializer
    adapter_class = TwitterOAuthAdapter
