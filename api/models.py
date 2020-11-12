from django.db import models

# Create your models here.


class Transaction(models.Model):
    """ Модель: Транзакция """
    name = models.TextField(verbose_name='Название транзакции')
    ticket = models.TextField(verbose_name='Тикет')
    price = models.FloatField(verbose_name='Цена транзакции')
    data = models.DateField(verbose_name='Дата совершения транзакции')
    active_type = models.PositiveIntegerField(verbose_name='Тип актива')

    class Meta:
        """ Мета класс """
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'

    def __str__(self):
        return f'{self.name}\t{self.price}'


class Contribution(models.Model):
    """ Модель: Вклад """
    name = models.TextField(verbose_name='Название вклада')
    percentage_rate = models.FloatField(verbose_name='Процентная ставка')
    current_amount = models.FloatField(verbose_name='Текущая сумма')
    percentage_accrual_date = models.DateField(verbose_name='Дата начисления процентов')
    percentage_to_contribution = models.BooleanField(default=False, verbose_name='Проценты начисляются на вклад')

    class Meta:
        """ Мета класс """
        verbose_name = 'Вклад'
        verbose_name_plural = 'Вклады'

    def __str__(self):
        return f'{self.name}\t{self.percentage_rate}\t{self.current_amount}'
