
from dj_rest_auth.registration.views import RegisterView
from rest_framework import serializers
from .serializers import SignupSerializer
from dj_rest_auth.views import LoginView
from rest_framework.permissions import AllowAny
from django_rest_passwordreset.views import ResetPasswordRequestToken, ResetPasswordConfirm, ResetPasswordValidateToken
from .serializers import PasswordResetTokenSerializer, UserProfileSerializer

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from ...models import User


class PasswordResetView(ResetPasswordRequestToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
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
