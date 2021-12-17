from rest_framework import serializers

from Api.models import Company

class CompanySerializer(serializers.ModelSerializer):

  class Meta:
    model = Company
    fields = '__all__'