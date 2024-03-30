from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.AccountView.as_view(), name='accounts'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('verification_link_sent/', views.VerificationLinkSentView.as_view(), name='verification_link_sent'),
    path('verify_email/<str:token>/', views.PasswordSetView.as_view(), name='password_set'),
    path('login/', views.LoginView.as_view(), name='login'),
]
