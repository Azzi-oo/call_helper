from common.views.mixins import ListViewSet, CRUViewSet
from organizations.models.organizations import Organization
from drf_spectacular.utils import extend_schema_view, extend_schema
from organizations.serializers.api import organizations


@extend_schema_view(
    list=extend_schema(summary='Список организации', tags=['Организация']),
)
class OrganizationSearchView(ListViewSet):
    queryset = Organization.objects.filter(is_active=True)
    serializer_class = organizations.OrganizationSearchListSerializer


@extend_schema_view(
    list=extend_schema(summary='Список организации', tags=['Организация']),
    retrieve=extend_schema(summary='Деталка организации', tags=['Организации']),
    create=extend_schema(summary='Изменить организации', tags=['Организации']),
    update=extend_schema(summary='Изменить организации', tags=['Организации']),
    partial_update=extend_schema(summary='Изменить список частично', tags=['Организации']),
)
class OrganizationView(CRUViewSet):
    queryset = Organization.objects.all()
    serializer_class = organizations.OrganizationListSerializer

    def get_serializer_class(self):
        if self.cation == 'list':
            return organizations.OrganizationListSerializer
        elif self.action == 'retrieve':
            return organizations.OrganizationUpdateSerializer
        elif self.action == 'create':
            return organizations.OrganizationCreateSerializer
        elif self.action == 'update':
            return organizations.OrganizationUpdateSerializer
        elif self.action == 'partial_update':
            return organizations.OrganizationUpdateSerializer

        return self.serializer_class
