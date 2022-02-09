from django.urls import path
from django.views.generic.base import TemplateView
from .views import SignUpView


urlpatterns = [
    path('Signup/', SignUpView.as_view(),name='signup'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', TemplateView.as_view(template_name='base.html')),
    path('', TemplateView.as_view(template_name='login.html')),
    path('', TemplateView.as_view(template_name='signup.html')),

]