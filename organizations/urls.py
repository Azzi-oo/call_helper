from django.urls import path, include
from users.serializers.api import users
from organizations.views.dicts import dicts, organizations, employees
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'dicts/positions', dicts.PositionView, 'positions')
router.register(r'search', organizations.OrganizationSearchView, 'organizations-search')
router.register(r'manage', organizations.OrganizationView, 'organizations')
router.register(r'manage/(?P<pk>\d+)/employees', employees.EmployeeView, 'employees')

urlpatterns = [
    path('organizations/', include(router.urls)),
]

# urlpatterns += path('organizations/', include(router.urls)),
