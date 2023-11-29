from common.views.mixins import ListViewSet, CRUDViewSet
from organizations.models.organizations import Organization, Employee
from drf_spectacular.utils import extend_schema_view, extend_schema
from organizations.serializers.api import employees as employees_s


@extend_schema_view(
    list=extend_schema(summary='Список организации', tags=['Организация']),
    retrieve=extend_schema(summary='Деталка организации', tags=['Организации']),
    create=extend_schema(summary='Изменить организации', tags=['Организации']),
    update=extend_schema(summary='Изменить организации', tags=['Организации']),
    partial_update=extend_schema(summary='Изменить список частично', tags=['Организации']),
    destroy=extend_schema(summary='Удалить сотрудника из организации', tags=['Организация']),
)
class EmployeeView(CRUDViewSet):
    queryset = Employee.objects.all()
    serializer_class = employees_s.EmployeeListSerializer

    lookup_url_kwarg = 'employee_id'

    def get_serializer_class(self):
        if self.cation == 'list':
            return employees_s.EmployeeListSerializer
        elif self.action == 'retrieve':
            return employees_s.EmployeeUpdateSerializer
        elif self.action == 'create':
            return employees_s.EmployeeCreateSerializer
        elif self.action == 'update':
            return employees_s.EmployeeUpdateSerializer
        elif self.action == 'partial_update':
            return employees_s.EmployeeUpdateSerializer

    def get_queryset(self):
        organization_id = self.request.parser_context['kwargs'].get('pk')

        queryset = Employee.objects.filter(
            organization_id=organization_id
        )
        return queryset
