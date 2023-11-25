from common.views.mixins import ExtendedGenericViewSet
from organizations.models.dicts import Position
from organizations.models.dicts import Position
from drf_spectacular.utils import extend_schema_view, extend_schema


@extend_schema_view(
    list=extend_schema(summary='Список должностей', tags=['Словари']),
)
class PositionView(ExtendedGenericViewSet):
    queryset = Position.objects.filter(is_active=True)
    serializer_class = Position
