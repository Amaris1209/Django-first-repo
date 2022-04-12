# from django.contrib.auth import get_user_model
from asyncore import read
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import fields
from django.http import HttpRequest
from django.utils.translation import ugettext_lazy as _
from allauth.account import app_settings as allauth_settings
from allauth.account.forms import ResetPasswordForm
from allauth.utils import email_address_exists, generate_unique_username
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
# from friends.api.serializers import FriendsSerializer
from rest_framework import serializers
from dj_rest_auth.serializers import PasswordResetSerializer
from django.conf import settings
from django_rest_passwordreset.serializers import PasswordTokenSerializer
from ...models import User
# User = get_user_model()
from allauth.account.forms import SignupForm
# from post.api.serializers import PostSerializer

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            },
            'email': {
                'required': True,
                'allow_blank': False,
            },
            'name': {
                'required': True,
                'allow_blank': False,
            }
        }

    def _get_request(self):
        request = self.context.get('request')
        if request and not isinstance(request, HttpRequest) and hasattr(request, '_request'):
            request = request._request
        return request

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def validate_password(self, password):
        return get_adapter().clean_password(password)

    def create(self, validated_data):
        user = User(
            email=validated_data.get('email'),
            name=validated_data.get('name'),
            username=generate_unique_username([
                validated_data.get('name'),
                validated_data.get('email'),
                'user'
            ])
        )
        user.set_password(validated_data.get('password'))
        user.save()
        request = self._get_request()
        setup_user_email(request, user, [])
        return user

    def save(self, request=None):
        """rest_auth passes request so we must override to accept it"""
        return super().save()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name']


class PasswordSerializer(PasswordResetSerializer):
    """Custom serializer for rest_auth to solve reset password error"""
    password_reset_form_class = ResetPasswordForm


class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """
    class Meta:
        model = User
        fields = ('id', 'external_id', 'username', 'email', 'name')
        read_only_fields = ('email', )


class PasswordResetTokenSerializer(PasswordTokenSerializer):
    password2 = serializers.CharField(label=_("Password2"), style={
                                      'input_type': 'password'})

    def validate(self, data):
        if data['password'] != data['password2']:
            raise ValidationError("The Two passwords don't match")
        return super().validate(data)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['external_id','id','email','name','profile_pic','role','country','zipCode','state','address']
        # fields ='__all__'