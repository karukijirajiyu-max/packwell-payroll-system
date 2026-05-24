import random
from django.core.mail import send_mail
from django.conf import settings


def generate_otp():
    return str(random.randint(100000, 999999))


def send_otp_email(email, otp):
    send_mail(
        'Your Login OTP',
        f'Your OTP code is: {otp}',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )