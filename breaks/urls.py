
from django.urls import path, include
from users.serializers.api import users
from organizations.views.dicts import dicts
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'dicts/statuses/breaks', dicts.BreakStatusView, 'breaks-statuses')
router.register(r'dicts/statuses/breaks', dicts.ReplacementStatusView, 'replacement-statuses')


urlpatterns = [
    
]

urlpatterns += path('organizations/', include(router.urls)),