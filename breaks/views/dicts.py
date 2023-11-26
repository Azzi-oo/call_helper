from drf_spectacular.utils import extend_schema_view, extend_schema
from breaks.serializers.api import dicts as dicts_s
from common.views.mixins import ListViewSet
from breaks.models.dicts import ReplacementStatus, BreakStatus


@extend_schema_view(
    list=extend_schema(summary='Список cтатусов смен', tags=['Словари']),
)
class ReplacementStatusView(ListViewSet):
    queryset = ReplacementStatus.objects.filter(is_active=True)
    serializer_class = dicts_s.ReplacementStatusListSerializer


@extend_schema_view(
    list=extend_schema(summary='Список статусов обеденных перерывов', tags=['Словари']),
)
class BreakStatusView(ListViewSet):
    queryset = BreakStatus.objects.filter(is_active=True)
    serializer_class = dicts_s.BreakStatusListSerializer
