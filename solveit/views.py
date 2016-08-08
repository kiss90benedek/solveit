from django.shortcuts import render

from solveit import helpers


def home(request):
    context = {
        'today': helpers.today(),
    }
    return render(request, 'index.html', context)
