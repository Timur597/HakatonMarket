from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView, DetailView, CreateView


def index(request):
    return render(request, 'base.html')

#
# class ProducerHome(ListView):
#     model = Producer
#     template_name = 'base.html'
#     context_object_name = 'producer'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['name'] = self.get_upper('Главная страница')
#         return context
#
#
# class Category(ListView):
#     model = ProductType
#     template_name = 'base.html'
#     context_object_name = 'category'
#     allow_empty = False
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = self.get_upper(ProductType.objects.get(pk=self.kwargs[
#              'category_id']))
#         return context
#
#
# class ProdHome(ListView):
#     model = Product
#     template_name = 'base.html'
#     context_object_name = 'product'
