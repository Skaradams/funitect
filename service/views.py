import os
import uuid
import hashlib

from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS

from funitect.service import models
from funitect import settings


__all__ = (
    'GameResource',
    'ElementKindResource',
    'ElementResource',
    'ElementCommentResource',
    'SketchResource',
)

@csrf_exempt 
def upload_sketch(request):
    response = HttpResponse(status=200)
    if request.method == 'POST':
        if 'sketch' in request.FILES:
            file_name = hashlib.md5(str(uuid.uuid1())).hexdigest()
            file_path = os.path.join(settings.SKETCHES_DIR, file_name)
            with open(file_path, 'wb') as sketch:
                sketch.write(request.FILES['sketch'].read())
            response.write('{"url": "/sketches/%s"}' % file_name)
        else:
            response.write('{"error": "No sketch file has been given"}' % file_name)
    return response

class ResourceAuthentication(BasicAuthentication):

    def is_authenticated(self, request, **kwargs):
        if request.user.is_authenticated():
            return True
        return super(
            ResourceAuthentication, self
        ).is_authenticated(request, **kwargs)


class OnlyUserContentAuthorization(DjangoAuthorization):

    def apply_limits(self, request, object_list):
        if request and hasattr(request, 'user'):
            return object_list.filter(
                user__pk=request.user.pk)
        return object_list.none()


class GameResource(ModelResource):

    class Meta:
        queryset = models.Game.objects.all()
        resource_name = 'game'
        allowed_methods = ['get', 'post', 'put']
        authentication = ResourceAuthentication()
        authorization = DjangoAuthorization()

class ElementKindResource(ModelResource):

    class Meta:
        queryset = models.ElementKind.objects.all()
        resource_name = 'element-kind'
        allowed_methods = ['get', 'post', 'put']
        authentication = ResourceAuthentication()
        authorization = DjangoAuthorization()

    def get_object_list(self, request):
        return super(
            ElementKindResource, self
        ).get_object_list(request).filter(game__id=request.GET['game'])

class ElementResource(ModelResource):

    class Meta:
        queryset = models.Element.objects.all()
        resource_name = 'element'
        allowed_methods = ['get', 'post']
        authentication = ResourceAuthentication()
        authorization = DjangoAuthorization()

    def get_object_list(self, request):
        return super(
            ElementResource, self
        ).get_object_list(request).filter(kind__id=request.GET['kind'])


class ElementCommentResource(ModelResource):

    class Meta:
        queryset = models.ElementComment.objects.all()
        resource_name = 'element-comment'
        allowed_methods = ['get', 'post']
        authentication = ResourceAuthentication()
        authorization = DjangoAuthorization()

    def dehydrate(self, bundle):
        bundle.data['user'] = bundle.obj.user.username
        return bundle

    def get_object_list(self, request):
        return super(
            ElementCommentResource, self
        ).get_object_list(request).filter(element__id=request.GET['element'])



class SketchResource(ModelResource):

    class Meta:
        queryset = models.ElementSketch.objects.all()
        resource_name = 'sketch'
        allowed_methods = ['get', 'post']
        authentication = ResourceAuthentication()
        authorization = DjangoAuthorization()

    def dehydrate(self, bundle):
        bundle.data['user'] = bundle.obj.user.username
        return bundle

    def get_object_list(self, request):
        return super(
            SketchResource, self
        ).get_object_list(request).filter(element__id=request.GET['element'])

