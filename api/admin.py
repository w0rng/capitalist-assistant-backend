from django.contrib import admin
import api.models as models
from random import randint


@admin.register(models.User)
class User(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'date_joined', 'get_token', 'age', 'gender')

    def get_token(self, obj):
        return obj.token[:5] + '*'*randint(3, 15) + obj.token[-5:]


admin.site.register(models.Credit)
