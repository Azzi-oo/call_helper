from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Break(models.Model):
    replacement = models.ForeignKey(
        'breaks.Replacement',
        on_delete=models.CASCADE,
        related_name='breaks',
        verbose_name='Смена',
    )
    employees = models.ForeignKey(
        to=User,
        related_name='breaks',
        on_delete=models.CASCADE,
        verbose_name='Сотрудник',
    )
    break_start = models.TimeField('Начало обеда', null=True, blank=True,)
    break_end = models.TimeField('Конец обеда', null=True, blank=True,)
    status = models.ForeignKey(
        'breaks.BreakStatus',
        models.RESTRICT,
        'breaks',
        verbose_name='Статус',
        blank=True
    )

    class Meta:
        verbose_name = 'Обеденный перерыв'
        verbose_name_plural = 'Обеденные перерывы'
        ordering = ('-replacement__date', 'breal_Start')

    def __str__(self):
        return f'Обед пользователя {self.employee} ({self.pk})'
