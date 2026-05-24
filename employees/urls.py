from django.urls import path
from .views import employee_login, verify_otp

urlpatterns = [
    path('login/', employee_login, name='employee_login'),
    path('verify-otp/', verify_otp, name='verify_otp'),
]
