from django.urls import path, include
from users.serializers.api import users
from organizations.views.dicts import dicts, organizations
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'dicts/positions', dicts.PositionView, 'positions')
router.register(r'search', organizations.OrganizationSearchView, 'organizations-search')

urlpatterns = [
    path('organizations/', include(router.urls)),
]

# urlpatterns += path('organizations/', include(router.urls)),
