from django.urls import path, include
from users.serializers.api import users
from users.views.users import RegistrationView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'search', users.UserSearchListSerializer, 'users-search')

urlpatterns = [
    path('users/reg/', users.RegistrationView.as_view(), name='reg'),
    path('users/me/', users.MeView.as_view(), name='me'),
    path('users/change-password/', users.ChangePasswordSerializer.as_view(), name='change_passwd'),
]

urlpatterns += path('users/', include(router.urls)),
