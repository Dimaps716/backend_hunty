# api/views.py
from django.shortcuts import render
from rest_framework import generics

from Api.models import Company
from Api.serializers import CompanySerializer


class CompanyList(generics.ListCreateAPIView):
  queryset = Company.objects.all()
  serializer_class = CompanySerializer

class companyDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Company.objects.all()
  serializer_class = CompanySerializer
