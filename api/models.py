from django.db import models

class Credit(models.Model):
    name = models.TextField(verbose_name='Название кредита')
    value = models.FloatField(verbose_name='Величина кредита')
    payment = models.FloatField(verbose_name='Ежемесячная выплата')


    def __str__(self):
        return f'{self.name}\t{self.value}\t{self.payment}'


    class Meta:
        verbose_name = u'Кредит'
        verbose_name_plural = u'Кредиты'
