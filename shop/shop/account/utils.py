from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


user = get_user_model()


class EmailVerify(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        user.name = None
        login_timestamp = (
            ""
            if user.name is None
            else user.name.replace(microsecond=0, tzinfo=None)
        )
        email_field = user.get_email_field_name()
        email = getattr(user, email_field, "") or ""
        return f"{user.id}{user.password}{login_timestamp}{timestamp}{email}"


def send_email_for_verify(request, user_with_id):
    obj = EmailVerify()
    current_site = get_current_site(request)

    context = {
        'user': user_with_id,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user_with_id.id)),
        'token': token_generator.make_token(user),
    }
    message = render_to_string('confirm_email.html', context)
    email = EmailMessage('Email verify', message, to=[user_with_id.email])
    email.send()



