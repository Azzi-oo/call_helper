from common.serializers.mixins import ExtendedView
from organizations.models.organizations import Organization, User
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


class OrganizationListSerializer(ExtendedView):
    director = UserShortSerializer()

    class Meta:
        model = Organization
        fields = '__all__'


class OrganizationRetrieveSerializer(ExtendedView):
    director = UserShortSerializer()

    class Meta:
        model = Organization
        fields = '__all__'


class OrganizationCreateSerializer(ExtendedView):
    director = UserShortSerializer()

    class Meta:
        model = Organization
        fields = (
            'id',
            'name',
        )


class OrganizationUpdateSerializer(ExtendedView):
    director = UserShortSerializer()

    class Meta:
        model = Organization
        fields = (
            'id',
            'name',
        )


class OrganizationEmployeeCreateSerializer(ExtendedView):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
            'position',
        )
