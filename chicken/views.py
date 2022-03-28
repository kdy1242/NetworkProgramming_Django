from django.shortcuts import render


def bbq(request):
    return render(request, 'chicken/bbq.html')


def goobne(request):
    return render(request, 'chicken/goobne.html')

