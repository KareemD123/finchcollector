from django.shortcuts import render, redirect

# Create your views here.

from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Add the following import
from django.http import HttpResponse

from .models import Finch
from .forms import FeedingForm
# from django.db import models


def home(request):
    # return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})


def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {'finch': finch, 'feeding_form': feeding_form})


def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)


class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    success_url = '/finches/'


class FinchUpdate(UpdateView):
    model = Finch
    # Let's disallow the renaming of a Finch by excluding the name field!
    # fields that will show up on the update form
    fields = ['breed', 'description', 'age']
    success_url = '/finches/'


class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'
