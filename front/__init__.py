import os

from django.template import Context, loader
from django.http import HttpResponse


def _get_app_pathes(extension):
    modules = []
    base_dir = os.path.join(os.path.dirname(__file__), 'app')
    os.path.walk(base_dir, lambda m, dir_name, file_names: m.extend([
        'app/' + os.path.relpath(os.path.join(
            dir_name, os.path.splitext(f)[0]
        ), base_dir) for f in file_names  if os.path.isfile(
            os.path.join(dir_name, f)
        ) and os.path.splitext(f)[1] == extension
    ]), modules)
    return modules


def index(request):
    t = loader.get_template('index.html')
    return HttpResponse(t.render(Context({
        'modules': _get_app_pathes('.js'),
        'templates': _get_app_pathes('.hbs'),
    })))
