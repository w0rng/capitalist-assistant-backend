from django.db.models import fields
from rest_framework import serializers
import api.models as models


class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contribution
        fields = '__all__'


class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
