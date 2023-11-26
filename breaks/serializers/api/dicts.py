from django.contrib.auth.password_validation import validate_password
from breaks.models import dicts
from django.contrib.auth import get_user_model
from common.serializers.mixins import ExtendedModelSerializer

User = get_user_model()


class ReplacementStatusListSerializer(ExtendedModelSerializer):
    class Meta:
        model = dicts.ReplacementStatus
        fields = (
            'code',
            'name',
            'color',
        )


class BreakStatusListSerializer(ExtendedModelSerializer):
    class Meta:
        model = dicts.BreakStatus
        fields = (
            'code',
            'name',
            'color',
        )
