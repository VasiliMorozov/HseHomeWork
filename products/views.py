from django.shortcuts import render

from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Product
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone


class DetailView(generic.DetailView):
    model = Product


class IndexView(generic.ListView):
    model = Product


class CreateView(generic.CreateView):
    model = Product
    fields = ['name', 'category']


class DeleteView(generic.DeleteView):
    model = Product
    success_url = reverse_lazy("products:index")

    def get(self, request, *args, **kwargs):
        print(request.method, request.path)
        return super().get(request, *args, **kwargs)


class UpdateView(generic.UpdateView):
    model = Product
    fields = ['name', 'category']


class DeprecatedUpdateView(generic.UpdateView):
    model = Product
    fields = ['name']


# def delete(request, pk):
#     if request.method == 'POST':
#         Product.objects.get(pk=pk).delete()
#         return HttpResponseRedirect(reverse('products:index'))
#     raise Http404()
