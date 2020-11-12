from django.contrib import admin
from .models import Transaction, Contribution

# Register your models here.

admin.site.register(Transaction)
admin.site.register(Contribution)
