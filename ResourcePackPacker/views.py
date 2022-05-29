import json

from django.http import HttpResponse
from django.shortcuts import render
from Packer.GetSponsors import GetSponsors


def hello(request):
    return HttpResponse("<h>Hello world ! </h>")


def test(request):
    a = GetSponsors()
    b = a.get_sponsors()
    c = []
    for i in b:
        c.append(f'<img src="{b[i]}" width="32">{i}')
    context = {'test': 'Test World!', 'x': json.dumps(c)}
    return render(request, 'test.html', context)

