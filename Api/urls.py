# django
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
# views
from Api.views import company, vacancy

urlpatterns = [
  # url of the api
  path('', vacancy.VacancyList.as_view()),
  path('vacancy/<int:pk>/', vacancy.VacancyDetail.as_view()),

  path('company', company.CompanyList.as_view()),
  path('company/<int:pk>/',company.companyDetail.as_view())

]