from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import get_object_or_404
import uuid

from .forms import CustomUserCreationForm, CustomSetPasswordForm, CustomAuthenticationForm
from .models import CustomUser

# Create your views here.

class AccountView(TemplateView):
    template_name = 'accounts/accounts.html'


class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = CustomUserCreationForm
    success_url = '/accounts/verification_link_sent/'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        birth_date = form.cleaned_data['birth_date']

        user = CustomUser.objects.create(name=name, email=email, birth_date=birth_date)
        token = str(uuid.uuid4())
        user.email_verification_token = token
        user.save()

        current_site = get_current_site(self.request)
        verification_link = f'http://{current_site}/accounts/verify_email/{token}/'

        subject = 'Twitter Email Verification'
        from_email = 'no-reply@twitter.com'
        message = f'Click the following link to verify your email\n{verification_link}'
        recipient_list = [user.email,]
        send_mail(subject, message, from_email, recipient_list)
        return super().form_valid(form)


class VerificationLinkSentView(TemplateView):
    template_name = 'accounts/verification_link_sent.html'


class PasswordSetView(FormView):
    template_name = 'accounts/password_set.html'
    form_class = CustomSetPasswordForm
    success_url = '/accounts/login/'

    def dispatch(self, request, *args, **kwargs):
        token = kwargs['token']
        user = get_object_or_404(CustomUser, email_verification_token=token)
        user.is_email_verified = True
        user.save()
        self.user = user
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.user
        return kwargs

    def form_valid(self, form):
        form.save()
        self.user.email_verification_token = None
        self.user.save()
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = CustomAuthenticationForm
    success_url = '/'