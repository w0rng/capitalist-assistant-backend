from django.contrib import admin
import api.models as models
from random import randint


@admin.register(models.User)
class User(admin.ModelAdmin):
    list_display = ('get_email', 'first_name', 'last_name', 'date_joined', 'get_token', 'age', 'gender')

    def get_token(self, obj):
        return obj.token[:5] + '*'*randint(3, 15) + obj.token[-5:]

    def get_email(self, obj):
        i = obj.email.index('@')
        return obj.email[:3] + '*'*randint(2, 7) + obj.email[i:]


@admin.register(models.Credit)
class Credit(admin.ModelAdmin):
    list_display = ('name', 'value', 'payment', 'user_id')


@admin.register(models.Contribution)
class Contribution(admin.ModelAdmin):
    list_display = ('name', 'percentage_rate', 'current_amount', 'percentage_accrual_date', 'percentage_to_contribution', 'user_id')

@admin.register(models.Transaction)
class Transaction(admin.ModelAdmin):
    list_display = ('name', 'ticket', 'price', 'data', 'active_type', 'user_id')
