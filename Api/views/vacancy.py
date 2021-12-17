from django.shortcuts import render
from rest_framework import generics

from Api.models import Vacancy
from Api.serializers import VacancySerializer

class VacancyList(generics.ListCreateAPIView):
  queryset = Vacancy.objects.all()
  serializer_class = VacancySerializer

class VacancyDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Vacancy.objects.all()
  serializer_class = VacancySerializer

