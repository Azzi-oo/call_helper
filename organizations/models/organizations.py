from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
User = get_user_model()
from common.models.mixins import InfoMixin, DateMixin


class Organization(InfoMixin):
    name = models.CharField("Название", max_length=150)
    director = models.ForeignKey(
        to=User,
        on_delete=models.RESTRICT,
        related_name='organization_directors',
        verbose_name='Директор',
    )
    employees = models.ManyToManyField(
        to=User,
        related_name='organization_employees',
        verbose_name='Сотрудники',
        blank=True,
    )

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.pk})'


class Group(InfoMixin):
    organization = models.ForeignKey(
        'breaks.Organization',
        on_delete=models.CASCADE,
        related_name='groups',
        verbose_name='Организация',
    )
    name = models.CharField('Название', max_length=255)
    manager = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        related_name='group_managers',
        verbose_name='Менеджер',
    )
    employees = models.ManyToManyField(
        User,
        'group_employees',
        verbose_name='Сотрудники',
        blank=True, through='Employee'
    )
    min_active = models.PositiveSmallIntegerField(
        'Минимальное количество активных сотрудников',
        null=True,
        blank=True,
    )
    break_start = models.TimeField('Начало обеда', null=True, blank=True,)
    break_end = models.TimeField('Конец обеда', null=True, blank=True,)
    break_max_duration = models.PositiveSmallIntegerField(
        'Максимальная длительность обеда',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.pk})'

    @property
    def break_duration(self):
        return 500


class Employee(models.Model):
    organization = models.ForeignKey(
        'Organization', models.CASCADE, 'employees_info',
    )
    user = models.ForeignKey(
        User, models.CASCADE, 'organization_info',
    )
    position = models.ForeignKey(
        'Position', models.RESTRICT, 'organization_info',
    )
    date_joined = models.DateField('Date joined', default=timezone.now)

    class Meta:
        verbose_name = 'Сотрудник организации'
        verbose_name_plural = 'Сотрудники организаций'
        ordering = ('-date_joined',)

    def __str__(self):
        return f'Employee {self.user}'