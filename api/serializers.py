from rest_framework import serializers
from .models import Contribution


class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = ('id',
                  'name', 
                  'percentage_rate', 
                  'current_amount', 
                  'percentage_accrual_date',
                  'percentage_to_contribution',
                  'user_id')