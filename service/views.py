import json
from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from funitect.service import models

__all__ = (
    'ItemResource',
)


class ResourceAuthentication(BasicAuthentication):

    def is_authenticated(self, request, **kwargs):
        if request.user.is_authenticated():
            return True
        return super(ResourceAuthentication, self).is_authenticated(
                                                        request, **kwargs)


class OnlyUserContentAuthorization(DjangoAuthorization):

    def apply_limits(self, request, object_list):
        if request and hasattr(request, 'user'):
            return object_list.filter(
                user__pk=request.user.pk)
        return object_list.none()


class ItemResource(ModelResource):

    class Meta:
        queryset = models.Item.objects.all()
        resource_name = 'game-info'
        allowed_methods = ['get', 'post', 'put']
        authentication = ResourceAuthentication()
        authorization = DjangoAuthorization()

