from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


def send_email_for_verify(request, user_with_id):
    current_site = get_current_site(request)

    context = {
        'user': user_with_id,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user_with_id.id)),
        'token': token_generator.make_token(user_with_id),
    }
    message = render_to_string('confirm_email.html', context)
    email = EmailMessage('Email verify', message, to=[user_with_id.email])
    email.send()



