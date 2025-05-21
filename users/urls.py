from django.urls import path
from django.contrib.auth import authenticate, views as auth_views

from . import views
from .forms import LoginForm

app_name = 'users'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm, next_page='users:profile'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', views.log_out, name='logout'),

    path('register/', views.register, name='register'),
    path('user/edit/', views.edit_user, name='user_edit'),

    path('ticket/', views.ticket, name="ticket"),

    path('password-change/', views.CustomPasswordChangeView.as_view(), name="password_change"),
    path('password-change/done/',
         views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name="password_change_done"),

    path('password-reset/', views.CustomPasswordResetView.as_view(), name="password_reset"),
    path('password-reset/done/',
         views.CustomPasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name="password_reset_done"),
    path('password-reset/<uidb64>/<token>/',
         views.CustomPasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path('password-reset/complete/',
         views.CustomPasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name="password_reset_complete"),

]
