from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):

    OTP_CHOICES = [
        ('email', 'Email'),
        ('sms', 'SMS'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    employee_id = models.CharField(
        max_length=20,
        unique=True
    )

    department = models.CharField(
        max_length=100
    )

    position = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    phone_number = models.CharField(
        max_length=20,
        blank=True
    )

    preferred_otp_method = models.CharField(
        max_length=10,
        choices=OTP_CHOICES,
        default='email'
    )

    otp_code = models.CharField(
        max_length=6,
        blank=True,
        null=True
    )

    otp_created_at = models.DateTimeField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.employee_id
    
class OTPVerification(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    otp_code = models.CharField(
        max_length=6
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_verified = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"{self.employee} - {self.otp_code}"