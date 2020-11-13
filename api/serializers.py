from django.db.models import fields
from rest_framework import serializers
import api.models as models

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = '__all__'