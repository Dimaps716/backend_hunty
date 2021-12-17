from django.contrib import admin

from Api.models import Company
from Api.models import Vacancy

class CompanyAdmin(admin.ModelAdmin):

  class Meta:
    model = Company
    fields = '__all__'


class VacancyAdmin(admin.ModelAdmin):

  class Meta:
    model = Vacancy
    fields = '__all__'


admin.site.register(Company, CompanyAdmin)
admin.site.register(Vacancy, VacancyAdmin)