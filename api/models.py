from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from api.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    GENDER = (
        (0, 'Ж'),
        (1, 'M')
    )

    email = models.EmailField(_('email'), unique=True)
    first_name = models.CharField(_('name'), max_length=30)
    last_name = models.CharField(_('surname'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('registered'), auto_now_add=True)
    token = models.CharField(_('token'), max_length=30, blank=False)
    age = models.IntegerField(_('age'), blank=True, default=0)
    gender = models.IntegerField(_('gender'), choices=GENDER, blank=True, default=0)

    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()

    def get_short_name(self):
        return self.first_name


class Credit(models.Model):
    name = models.TextField(verbose_name='Название кредита')
    value = models.FloatField(verbose_name='Величина кредита')
    payment = models.FloatField(verbose_name='Ежемесячная выплата')


    def __str__(self):
        return f'{self.name}\t{self.value}\t{self.payment}'


    class Meta:
        verbose_name = u'Кредит'
        verbose_name_plural = u'Кредиты'
