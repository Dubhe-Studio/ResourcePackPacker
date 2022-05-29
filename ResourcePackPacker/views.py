import json
from django.shortcuts import render
from Packer.GetSponsors import GetSponsors


def test(request):
    a = GetSponsors()
    b = a.get_sponsors()
    c = []
    for i in b:
        c.append(f'<img src="{b[i]}" width="32">{i}')
    context = {'x': json.dumps(c)}
    return render(request, 'test.html', context)

