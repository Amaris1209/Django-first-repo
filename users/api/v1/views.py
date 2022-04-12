
from email import message
from dj_rest_auth.registration.views import RegisterView
from .utils import Util
from django_rest_passwordreset.models import ResetPasswordToken
from django_rest_passwordreset.tokens import get_token_generator
from rest_framework import serializers

from users.service import get_token
from .serializers import SignupSerializer
from dj_rest_auth.views import LoginView
from rest_framework.permissions import AllowAny
from django_rest_passwordreset.views import HTTP_IP_ADDRESS_HEADER, HTTP_USER_AGENT_HEADER, ResetPasswordRequestToken, ResetPasswordConfirm, ResetPasswordValidateToken
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PasswordResetTokenSerializer, UserProfileSerializer
# from .utils import Util
from ...models import User
from django.utils.crypto import get_random_string


class SendInvite(ResetPasswordRequestToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        # if response.status_code == 200:
        #     print(request.data['email'])
        #     user = User.objects.get(email=request.data['email'])
        #     # token = get_random_string(length=6, allowed_chars='1234567890')
        #     # token = get_token()
        #     token = ResetPasswordToken.objects.create(
        #         user=user,
        #         user_agent=request.META.get(HTTP_USER_AGENT_HEADER, ''),
        #         ip_address=request.META.get(HTTP_IP_ADDRESS_HEADER, ''),
        #     )
        data = {'email_body': request.data['message']
        # +"\n"+"https://ready-shout-30574.botics.co/claim-profile" 
        , 'to_email': request.data['email'],

        'email_subject': 'Send email for Your Ride'}

        Util.send_email(data)

        response.data["detail"] = "Email has been sent."

        return response




class PasswordResetView(ResetPasswordRequestToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            print(request.data['email'])
            user = User.objects.get(email=request.data['email'])
            # token = get_random_string(length=6, allowed_chars='1234567890')
            # token = get_token()
            token = ResetPasswordToken.objects.create(
                user=user,
                user_agent=request.META.get(HTTP_USER_AGENT_HEADER, ''),
                ip_address=request.META.get(HTTP_IP_ADDRESS_HEADER, ''),
            )
            print(token.key)
            data = {'email_body': 'Reset token for Your Ride is '+token.key, 'to_email': request.data['email'],
                    'email_subject': 'Reset your passsword'}
            Util.send_email(data)
            response.data["detail"] = "Password reset e-mail has been sent."
        return response


class PasswordResetConfirmView(ResetPasswordConfirm):
    serializer_class = PasswordResetTokenSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            response.data["detail"] = "Password has been reset successfuly"

        return response


class ResetPasswordVerifyToken(ResetPasswordValidateToken):
    def post(self, request, *args, **kwargs):

        response = super().post(request, *args, **kwargs)
        return response


class UserLoginView(LoginView):
    permission_classes = [AllowAny]


class UserRegisterView(RegisterView):
    serializer_class = SignupSerializer


class UserProfileView(RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    model = User

    def get_object(self):
        return self.request.user
