from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordChangeDoneView, \
    PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView
from django.urls import reverse_lazy
import jdatetime
from datetime import datetime

from .forms import *


# Create your views here.


def profile(request):
    now = datetime.now()
    persian_date = jdatetime.datetime.fromgregorian(datetime=now)
    context = {
        'user': request.user,
        'persian_date': persian_date.strftime('%A %d %B %Y - %H:%M'),
    }
    return render(request, 'users/profile.html', context)


def log_out(request):
    logout(request)
    return render(request, "registration/logged_out.html")


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'registration/register_done.html', {'user': user})
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def edit_user(request):
    if request.method == 'POST':
        form = UserEditForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UserEditForm(instance=request.user)

    return render(request, 'registration/edit_user.html', {'form': form})


def ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            subject = data['subject']
            message = f"{data['name']}\n{data['email']}\n{data['phone']}\n\n{data['message']}"
            from_email = 'avaghiasian82@gmail.com'
            to_email = ['avaghiasian03@gmail.com']
            send_mail(subject, message, from_email, to_email, fail_silently=False)
            messages.success(request, 'پیام شما با موفقیت ارسال شد.')
    else:
        form = TicketForm()
    return render(request, "users/forms/ticket.html", {'form': form})


class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'users/forms/password_change.html'
    success_url = reverse_lazy('users:password_change_done')


class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'users/forms/password_change_done.html'


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'users/forms/password_reset.html'
    email_template_name = 'forms/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/forms/password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/forms/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/forms/password_reset_complete.html'
