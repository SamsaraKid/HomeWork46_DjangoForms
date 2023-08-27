from django.shortcuts import render
from anketa.myforms import NashaForma
from anketa.myforms import AniForma
from django.http import HttpResponse

# Create your views here.


def index(req):
    return render(req, 'index.html')


def forma1(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        num = req.POST.get('num')
        out = '<h1>Спасибо</h1>' \
              '<h2>Ваше имя - {0}</h2>' \
              '<h2>Ваше число - {1}</h2>' \
              '<div class="center"><a href="/"><button>На главную</button></a></div>'.format(name, num)
        return HttpResponse(out)
    else:
        anketa1 = NashaForma()
        data = {'form': anketa1}
        return render(req, 'forma.html', context=data)


def forma2(req):
    if req.method == 'POST':
        img = req.FILES['img']
        file = open('anketa/static/upload/' + img.name, 'wb+')
        file.write(img.read())
        file.close()
        data = {'name': req.POST.get('name'),
                'breed': req.POST.get('breed'),
                'age': req.POST.get('age'),
                'color': req.POST.get('color'),
                'food': req.POST.get('food'),
                'img': '/upload/' + img.name}
        return render(req, 'final.html', context=data)
    else:
        anketa2 = AniForma()
        data = {'form': anketa2}
        return render(req, 'forma.html', context=data)


