import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    # WARNING!
    """
    Some officially supported features of Crowdbotics Dashboard depend on the initial
    state of this User model (Such as the creation of superusers using the CLI
    or password reset in the dashboard). Changing, extending, or modifying this model
    may lead to unexpected bugs and or behaviors in the automated flows provided
    by Crowdbotics. Change it at your own risk.


    This model represents the User instance of the system, login system and
    everything that relates with an `User` is represented by this model.
    """

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, null=True, max_length=255)
    external_id = models.UUIDField(verbose_name=_("External user id"),
                                   blank=True, default=uuid.uuid4,)
    profile_pic = models.TextField(default="")
    role = models.CharField(max_length = 255, blank=True, null=True,)
    address = models.CharField(max_length = 255, blank=True, null=True,)
    state = models.CharField(max_length = 255, blank=True, null=True,)
    zipCode = models.CharField(max_length = 255, blank=True, null=True,)
    country = models.CharField(max_length = 255, blank=True, null=True,)
    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class UserResetToken(models.Model):
    token = models.CharField(verbose_name=_("reset token"), max_length=20)
    updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    #email = models.EmailField(verbose_name=_("Email"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)