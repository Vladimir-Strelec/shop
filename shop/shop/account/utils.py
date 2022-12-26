from distlib.compat import text_type
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.conf import settings

from shop.settings import EMAIL_HOST_USER


class AppTokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        return text_type((user.is_active + user.pk + timestamp))


def send_email_for_verify(request, user_with_id):
    current_site = get_current_site(request)

    context = {
        'user': user_with_id,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user_with_id.id)),
        'token': token_generator.make_token(user_with_id),
    }
    message = render_to_string('confirm_email.html', context=context)
    email = EmailMessage('Email verify', message, to=[user_with_id.email])
    send_mail('Contact form', message=message, from_email=EMAIL_HOST_USER, recipient_list=['vovik050github@gmail.com'], fail_silently=False)

    # email.send()



# from utils.mails import send_conf_mail
# from utils.tokens import token_generator
# from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from urllib3.packages.six import text_type
#
#
# class AppTokenGenerator(PasswordResetTokenGenerator):
#     def _make_hash_value(self, user, timestamp):
#         return text_type((user.is_active + user.pk + timestamp))
#
#
token_generator = AppTokenGenerator()