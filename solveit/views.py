from datetime import date
from django.shortcuts import render


def home(request):
    context = {
        'today': date.today(),
    }
    return render(request, 'index.html', context)
