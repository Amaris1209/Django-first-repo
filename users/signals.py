from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse
from django.db.models.signals import post_save
from .models import Invitation

from django_rest_passwordreset.signals import reset_password_token_created
from django_rest_passwordreset.models import get_password_reset_token_expiry_time
from datetime import timedelta


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    # get token expiration time
    expire_time = timedelta(hours=get_password_reset_token_expiry_time())
    # send an e-mail to the user
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        # 'reset_password_url': "{}?token={}".format(
        #     instance.request.build_absolute_uri(reverse('password_reset:reset-password-confirm')),
        #     reset_password_token.key)
        'token': reset_password_token.key ,
        'expire_time': expire_time,

    }
    # render email text
    email_html_message = render_to_string('email/user_reset_password.html', context)
    email_plaintext_message = render_to_string('email/user_reset_password.txt', context)
    from_email = settings.DEFAULT_FROM_EMAIL

    msg = EmailMultiAlternatives(
        # title:
        "Password Reset for {title}".format(title=" Your Ride app"),
        # message:
        email_plaintext_message,
        # from:
        from_email,
        # to:
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()

# @receiver(post_save,sender=Invitation)
# def sent_inivitation_email(sender, instance, **kwargs):

#     context = {
#         'inviter': instance.inviter,
#          "username": instance.username if instance.username else "there",
#     }
#     # render email text
#     email_html_message = render_to_string('email/invitation.html', context)
#     email_plaintext_message = render_to_string('email/invitation.txt', context)
#     from_email = settings.DEFAULT_INVITATION_EMAIL

#     msg = EmailMultiAlternatives(
#         # title:
#         "Invitation to use {title}".format(title=" Bottled&Blended app"),
#         # message:
#         email_plaintext_message,
#         # from:
#         from_email,
#         # to:
#         [instance.email]
#     )
#     msg.attach_alternative(email_html_message, "text/html")
#     #print("email sent")
#     #TODO add field to database to show if message sent
#     msg.send()