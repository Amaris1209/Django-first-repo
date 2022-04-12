from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from users.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)
from .views import SendInvite,  UserRegisterView, UserLoginView, PasswordResetView,\
    PasswordResetConfirmView, ResetPasswordVerifyToken,\
    UserProfileView
from rest_auth.registration.views import VerifyEmailView, RegisterView
from dj_rest_auth.views import PasswordChangeView
router = DefaultRouter()
#router.register("signup", SignupViewSet, basename="signup")
#router.register("login", LoginViewSet, basename="login")

urlpatterns = [
    path("profile/", UserProfileView.as_view(), name="api-users-profile"),
    # user Authentications API
    #path("", include(router.urls)),
    path("signup/", UserRegisterView.as_view(), name='api-signup'),
    path("login/", UserLoginView.as_view(), name='api-login'),
    
    #path('password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('password/reset/', PasswordResetView.as_view(), name='api-rest_password'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(),
         name='api-rest_password_confirm'),
    path('password/reset/verify-token/',
         ResetPasswordVerifyToken.as_view(), name='api-rest_password'),
    path('password/change/', PasswordChangeView.as_view(),
         name='api-rest_password_change'),
    # path("password/reset/", PasswordResetView.as_view(), name = "password-reset"),
    path("social-auth/", include('users.api.v1.social-auth.urls')),
    path('SendInvite/', SendInvite.as_view(), name='api-SendInvite'),
    # path('logout/',LogoutView.as_view()),
]

if getattr(settings, 'REST_USE_JWT', False):
    from rest_framework_simplejwt.views import TokenVerifyView

    from dj_rest_auth.jwt_auth import get_refresh_view

    urlpatterns += [
        path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
        path('token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
    ]
