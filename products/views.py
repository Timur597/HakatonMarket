from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'base.html')

# def post_list(request):
#     return render(request, 'base.html', {})

# class ProdHome(ListView):
#     model = Producer
#     template_name = 'base.html'
#     context_object_name = 'producer'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = self.get_upper('Главная страница')
#         return context