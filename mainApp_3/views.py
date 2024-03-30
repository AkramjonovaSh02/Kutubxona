from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def home(request):
    return HttpResponse('DAstur ishladi')



def kutubxonachi_tahrirlash(request):
    kutubxonachi = Kutubxonachi.objects.filter(id=pk)
    if request.method == 'POST':
        kutubxonachi.update(
            ism = request.POST.get('ism'),
            ish_vaqti = request.POST.get('ish_vaqti')
        )
        return redirect('/kutubxonachilar/')
    context = {
        'kutubxonachi': kutubxonachi.first()
    }
    return render(request, 'Kutubxonachi.html', context)

def add_muallif(request):
    if request.method == 'POST':
        form = MuallifForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mualliflar')  # Предположим, что 'index' - это ваше представление для отображения списка муаллифов
    else:
        form = MuallifForm()
    return render(request, 'add_muallif.html', {'form': form})

def add_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/recordlar')
    else:
        form = RecordForm()
    return render(request, 'add_record.html', {'form': form})

def add_kutubxonachi(request):
    if request.method == 'POST':
        form = KutubxonachiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/kutuxonachilar')
    else:
        form = KutubxonachiForm()
    return render(request, 'add_kutubxonachi.html', {'form': form})