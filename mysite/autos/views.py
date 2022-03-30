from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy #reverse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from autos.models import Auto, Make
# from autos.forms import MakeForm, AutoForm

# Create your views here.

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        make  = Make.objects.all().count()
        auto = Auto.objects.all()
        context = {'make_count': make, 'auto_list': auto}
        return render(request, 'autos/auto_list.html', context)

class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        make = Make.objects.all()
        context = {'make_list': make}
        return render(request, 'autos/make_list.html', context)

class MakeCreate(LoginRequiredMixin, CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')
class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')
class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


"""
# Above is the shorter version
# This commented code is the representation of using Forms with Models.
# BY creating  get and post function the corresponding action is done by both aspects in application.
# There is Creating, Updating and Deleting which have different behaviors on how post and get function
# ** remember post is to when yuou want to save, udate or delete data while get is for wanting to view or read data
# This also involves having to create a Form object int he forms.py but Django has a shorter way of doing it
# Using inheritance of a class functions CreateView, UpdateView, and DeleteView which basically do what Is done below
# it is all under the hood done for you
# We use reverse_lazy rather than reverse in the class attributes
# because views.py is loaded by urls.py and in urls.py as_view() causes
# the constructor for the view class to run before urls.py has been
# completely loaded and urlpatterns has been processed.

# References
# https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-editing/#createview
class MakeCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = MakeForm()
        context = {'form': form}
        return render(request, 'autos/make_form.html', context)
    def post(self, request):
        form = MakeForm(request.POST)
        if not form.is_valid():
            context = {'form': form}
            return render(request, 'autos/make_form.html', context)
        # save the form and get a model object
        new_make = form.save()
        success_url = reverse('autos:all')
        return redirect(success_url)
class MakeUpdate(LoginRequiredMixin, View):
    def get(self, request, pk):
        old_make = get_object_or_404(Make, pk = pk)
        form = MakeForm(instance=old_make)
        context = {'form':form}
        return render(request, 'autos/make_form.html', context)

    def post(self, request, pk):
        old_make = get_object_or_404(Make, pk=pk)
        form = MakeForm(request.POST, instance=old_make)
        if not form.is_valid():
            context = {'form': form}
            return render(request, 'autos/make_form.html', context)

        form.save()
        success_url = reverse('autos:all')
        return redirect(success_url)
class MakeDelete(LoginRequiredMixin, View):
    def get(self, request, pk):
        old_make = get_object_or_404(Make, pk=pk)
        form = MakeForm(instance=old_make)
        context = {'form': form}
        return render(request, 'autos/make_confirmation_delete.html', context)
    def post(self, request, pk):
        old_make = get_object_or_404(Make, pk=pk)
        old_make.delete()
        success_url = reverse('autos:all')
        return redirect(success_url)


class AutoCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = AutoForm()
        context = {'form': form}
        return render(request, 'autos/auto_form.html', context)
    def post(self, request):
        form = AutoForm(request.POST)
        if not form.is_valid():
            context = {'form': form}
            return render(request, 'autos/auto_form.html', context)
        # save the form and get a model object
        new_auto = form.save()
        success_url = reverse('autos:all')
        return redirect(success_url)


class AutoUpdate(LoginRequiredMixin, View):
    def get(self, request, pk):
        old_auto = get_object_or_404(Auto, pk = pk)
        form = AutoForm(instance=old_auto)
        context = {'form':form}
        return render(request, 'autos/auto_form.html', context)

    def post(self, request, pk):
        old_auto = get_object_or_404(Auto, pk=pk)
        form = AutoForm(request.POST, instance=old_auto)
        if not form.is_valid():
            context = {'form': form}
            return render(request, 'autos/auto_form.html', context)

        form.save()
        success_url = reverse('autos:all')
        return redirect(success_url)


class AutoDelete(LoginRequiredMixin, View):
    def get(self, request, pk):
        old_auto = get_object_or_404(Auto, pk=pk)
        form = AutoForm(instance=old_auto)
        context = {'form': form}
        return render(request, 'autos/auto_confirmation_delete.html', context)
    def post(self, request, pk):
        old_auto = get_object_or_404(Auto, pk=pk)
        old_auto.delete()
        success_url = reverse('autos:all')
        return redirect(success_url)
"""

