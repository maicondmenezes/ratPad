from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login'
    template_name = 'home.html'

class AboutPageView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login'
    template_name = 'about.html'

class NotFoundPageView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login'
    template_name = '404.html'
