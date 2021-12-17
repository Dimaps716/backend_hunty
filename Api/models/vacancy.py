from django.db import models
from Api.models import Company

class Vacancy(models.Model):
  """
  represent Vacancy
  """
  ACTIVE = 'ACTIVE'
  FINALIZE = 'FINALIZE'

  CHICES_STATUS_VACANTE =[
    (ACTIVE, 'ACTIVE'),
    (FINALIZE, 'FINALIZE')
  ]

  VacancyId = models.AutoField(primary_key=True)
  PositionName = models.CharField(max_length=100, blank=False, null=False)
  VacancyLink = models.URLField(null=True, blank=True)
  CompanyId = models.ForeignKey(Company, on_delete= models.CASCADE)
  Salary = models.IntegerField()
  Skills = models.TextField(null=True, blank=True)
  MaxExperience = models.IntegerField()
  MinExperience = models.IntegerField()
  status = models.CharField(
    choices=CHICES_STATUS_VACANTE, default=ACTIVE, max_length=15
  )

  # Return positionName
  def __str__(self):
    return self.PositionName

    class Meta:
      verbose_name = 'Vacancy'
      verbose_name_plural = 'Vacancies'
      ordering = ['id']