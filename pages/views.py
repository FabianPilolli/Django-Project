from django.shortcuts import render
# generic views to work with templates
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"