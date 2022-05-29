from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("<h>Hello world ! </h>")


def test(request):
    context = {'test': 'Test World!'}
    return render(request, 'test.html', context)

