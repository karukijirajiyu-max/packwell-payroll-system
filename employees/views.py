import random

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .models import Employee, OTPVerification
from .utils import send_otp_email


def employee_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            employee = Employee.objects.get(user=user)

            otp = str(random.randint(100000, 999999))

            OTPVerification.objects.create(
                employee=employee,
                otp_code=otp
            )

            send_otp_email(
                employee.email,
                otp
            )

            request.session['user_id'] = user.id

            return redirect('verify_otp')

    return render(request, 'login.html')


def verify_otp(request):

    if request.method == 'POST':

        otp = request.POST['otp']

        user_id = request.session.get('user_id')

        employee = Employee.objects.get(
            user_id=user_id
        )

        latest_otp = OTPVerification.objects.filter(
            employee=employee
        ).last()

        if latest_otp and latest_otp.otp_code == otp:

            login(request, employee.user)

            latest_otp.is_verified = True
            latest_otp.save()

            return redirect('/')

    return render(request, 'verify_otp.html')