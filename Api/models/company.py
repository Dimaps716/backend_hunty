from django.db import models

class Company(models.Model):
  CompanyId = models.AutoField(primary_key=True)
  Name = models.CharField(max_length=100, null=False, blank=False)
  Link = models.URLField(null=True,blank=True)
  Country = models.CharField(max_length=100)
  City = models.CharField(max_length=100)
  DateAdded  = models.DateField()
  ContactFirstName = models.CharField(max_length=100)
  ContactLastName =  models.CharField(max_length=100)
  ContactPhoneNumber = models.CharField(max_length=100, null=True, blank=True)
  ContactEmail = models.EmailField()

  # Return Name
  def __str__(self):
    return self.Name

    class Meta:
      verbose_name = 'company'
      verbose_name_plural = 'companies'
      ordering = ['id']