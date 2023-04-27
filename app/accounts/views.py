from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from shortener.models import ShortURL


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ProfileView(LoginRequiredMixin, ListView):
    template_name = 'accounts/profile.html'

    def get_queryset(self):
        return ShortURL.objects.filter(owner=self.request.user)
