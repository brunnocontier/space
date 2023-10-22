from django.shortcuts import render


def index(request):

    dados = {
        1: {'nome': 'Nebulosa de Carina', 'fonte': 'webbtelescope.org - NASA - JAMES WEBB'},
        2: {'nome': 'Galaáxia NGC 1079', 'fonte': 'nasa.org - NASA - HUBBLE'},
        3: {'nome': 'Galaáxia NGC 1079', 'fonte': 'nasa.org - NASA - HUBBLE'}
    }
    return render(request, 'galery/index.html', {'cards': dados})


def image(request):
    return render(request, 'galery/image.html')