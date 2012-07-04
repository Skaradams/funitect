import os
import uuid
import hashlib
import Image

from django.views.decorators.csrf import csrf_exempt
from django import http

from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization

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
    response = http.HttpResponse(status=200)
    if request.method == 'POST':
        if 'sketch' in request.FILES:
            file_name = hashlib.md5(
                str(uuid.uuid1())
            ).hexdigest() + '_' + request.FILES['sketch'].name
            file_path = os.path.join(settings.SKETCHES_DIR, file_name)
            tmp_file_path = os.path.join('/tmp', file_name)
            with open(tmp_file_path, 'wb') as sketch_tmp:
                sketch_tmp.write(request.FILES['sketch'].read())
            try:
                image = Image.open(tmp_file_path)
                image.save(file_path)
            except Exception, e:
                raise ValueError(str(e))
            response.write('{"url": "/sketches/%s"}' % file_name)
        else:
            response.write(
                '{"error": "No sketch file has been given"}')
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

    def hydrate(self, bundle):
        if bundle.request.user.is_authenticated() \
                    and bundle.request.method == 'POST':
            bundle.obj.user = bundle.request.user
            bundle.obj.kind = models.ElementKind.objects.get(
                id=int(bundle.request.GET['kind'])
            )
            bundle.obj.name = bundle.request.GET['name']
        return bundle

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

    def hydrate(self, bundle):
        if bundle.request.user.is_authenticated() \
                        and bundle.request.method == 'POST':
            bundle.obj.user = bundle.request.user
            bundle.obj.element = models.Element.objects.get(
                id=int(bundle.request.GET['element'])
            )
            bundle.obj.text = bundle.request.GET['text']
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
        if bundle.request.method == 'GET':
            bundle.data['user'] = bundle.obj.user.username
        return bundle

    def hydrate(self, bundle):
        if bundle.request.user.is_authenticated() \
                    and bundle.request.method == 'POST':
            bundle.obj.user = bundle.request.user
            bundle.obj.element = models.Element.objects.get(
                id=int(bundle.request.GET['element'])
            )
            bundle.obj.src = bundle.request.GET['src']
        return bundle

    def get_object_list(self, request):
        obj_list = super(SketchResource, self).get_object_list(request)
        if request.method == 'GET':
            obj_list = obj_list.filter(element__id=request.GET['element'])
        return obj_list
