from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ReplacementStatus(models.Model):
    code = models.CharField('Код', max_length=16, primary_key=True)
    name = models.CharField('Название', max_length=32,)
    sort = models.PositiveSmallIntegerField('Сортировка', null=True, blank=True)
    is_active = models.BooleanField('Активность', default=True)

    class Meta:
        verbose_name = 'Статус смены'
        verbose_name_plural = 'Статусы смены'
        ordering = ('sort',)

    def __str__(self):
        return f'Смена №{self.code} для {self.name}'


class Replacement(models.Model):
    group = models.ForeignKey(
        'breaks.Group',
        on_delete=models.CASCADE,
        related_name='replacements',
        verbose_name='Директор',
    )
    date = models.DateField('Дата смены')
    break_start = models.TimeField('Начало обеда')
    break_end = models.TimeField('Конец обеда')
    break_max_duration = models.PositiveSmallIntegerField(
        'Максимальная продолжительность обеда'
    )

    class Meta:
        verbose_name = 'Смена'
        verbose_name_plural = 'Смены'
        ordering = ('-date',)

    def __str__(self):
        return f'Смена №{self.pk} {self.group}'


class ReplacementEmployee(models.Model):
    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='replacements',
        verbose_name='Группа',
    )
    replacement = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='employees',
        verbose_name='Смена'
    )
    status = models.ForeignKey(
        'breaks.Replacement',
        on_delete=models.RESTRICT,
        'replacement_employees',
        verbose_name='Статус'
    )
    class Meta:
        verbose_name = 'Смена - Работник'
        verbose_name_plural = 'Смены - Работники'
        ordering = ('-date',)

    def __str__(self):
        return f'Смена {self.replacement} для {self.group}'