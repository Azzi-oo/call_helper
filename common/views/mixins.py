from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins


class ExtendedGenericViewSet(GenericViewSet):
    class Meta:
        pass


class ListViewSet(ExtendedGenericViewSet, mixins.ListModelMixin):
    pass


class CRUViewSet(ExtendedGenericViewSet,
                 mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.ListModelMixin):
    pass


class CRUDViewSet(CRUViewSet,
                  mixins.DestroyModelMixin):
    pass


# class DictListMixin(ListViewSet):
#     serializer_class = DictMixinSerializer
#     pagination_class = None
