from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from funitect.service import models

__all__ = (
    'GameResource',
    'ElementKindResource',
)


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