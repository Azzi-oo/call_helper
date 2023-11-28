from common.serializers.mixins import ExtendedView
from organizations.models.organizations import Organization
from organizations.serializers.nested.users import UserShortSerializer


class OrganizationSearchListSerializer(ExtendedView):
    director = UserShortSerializer()

    class Meta:
        model = Organization
        fields = (
            "id",
            "name",
            "director",
        )
