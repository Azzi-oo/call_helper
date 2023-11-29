from common.serializers.mixins import ExtendedView
from organizations.models.organizations import Employee
from organizations.models.organizations import Organization, User
from rest_framework import serializers


User = get_user

class EmployeeListSerializer(ExtendedView):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeCreateSerializer(ExtendedView):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = Employee
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
            'position',
        )

    def validate(self, attrs):
        current_user = get_current_user()
        organization_id = attrs['organization'] = self.context['view'].kwargs.get('id')
        organization = Organization.objects.filter(
            id=organization_id, director=current_user,
        ).first()
        if not organization:
            raise ParseError(
                'Такой организации не найдено'
            )

        attrs['organization'] = organization
        return attrs

    def create(self, validated_data):
        user_data = {
            'first_name': validated_data.pop('first_name'),
            'last_name': validated_data.pop('last_name'),
            'email': validated_data.pop('email'),
            'password': validated_data.pop('password'),
            'is_corporate_account': True,
        }
        with transaction.atomic():
            user = User.objects.create_user(**user_data)
            validated_data['user'] = user

            instance = super().create(validated_data)
        return instance
