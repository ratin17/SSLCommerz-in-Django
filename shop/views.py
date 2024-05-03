from django.shortcuts import render

#models
from .models import Product

# import views
from django.views.generic import ListView, DetailView

#mixin
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(ListView):
    model = Product
    template_name = 'home.html'


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product_detail.html'