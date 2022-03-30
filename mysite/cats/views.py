from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.urls import reverse_lazy
from .models import Breed, Cat
# Create your views here.

class CatView(LoginRequiredMixin, View):
    def get(self, request):
        breed = Breed.objects.all().count()
        cat = Cat.objects.all()
        context = {'breed_count':breed, 'cat_list':cat}
        return render(request, 'cats/cat_list.html', context)

class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        breed = Breed.objects.all()
        context = {'breed_list':breed}
        return render(request, 'cats/breed_list.html', context)


class BreedCreate(LoginRequiredMixin, CreateView):
    # template_name = 'cats/cat_form.html'
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all_cats')

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all_cats')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all_cats')


class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all_cats')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all_cats')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all_cats')
        
