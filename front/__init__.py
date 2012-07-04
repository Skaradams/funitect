from django.template import Context, loader
from django.http import HttpResponse


def index(request):
    t = loader.get_template('index.html')
    return HttpResponse(t.render(Context()))
