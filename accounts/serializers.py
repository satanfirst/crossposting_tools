from allauth.socialaccount.helpers import complete_social_login
from dj_rest_auth.registration.serializers import SocialLoginSerializer
from django.utils.translation import ugettext_lazy as _
from requests.exceptions import HTTPError
from rest_framework import serializers
from django.contrib.auth.models import User


class VKOAuth2Serializer(SocialLoginSerializer):
    user_id = serializers.CharField(required=True)
    email = serializers.CharField(required=False, allow_blank=True)
    profile_pk = serializers.CharField(required=False, allow_blank=True)

    def validate(self, attrs, profile_pk=None):
        view = self.context.get('view')
        request = self._get_request()

        if not view:
            raise serializers.ValidationError(_("View is not defined, pass it as a context variable"))

        adapter_class = getattr(view, 'adapter_class', None)
        if not adapter_class:
            raise serializers.ValidationError(_("Define adapter_class in view"))

        adapter = adapter_class(request)
        app = adapter.get_provider().get_app(request)

        # Case 1: We received the access_token
        if attrs.get('access_token'):
            if not attrs.get('user_id'):
                raise serializers.ValidationError(_("Incorrect input. user_id is required with access_token."))

            access_data = {
                'access_token': attrs.get('access_token'),
                'user_id': attrs.get('user_id'),
            }

        social_token = adapter.parse_token({'access_token': access_data['access_token']})
        social_token.app = app
        try:
            login = self.get_social_login(adapter, app, social_token, access_data)
            if profile_pk:
                new_user = User.objects.get(pk=profile_pk)
            complete_social_login(request, login)
        except HTTPError:
            raise serializers.ValidationError(_('Incorrect value'))

        if not login.is_existing:
            login.lookup()
            login.save(request, connect=True)

        attrs['user'] = login.account.user

        return attrs
