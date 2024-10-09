from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class cv_user(models.Model):
   name     = models.CharField('name', max_length=80, default='John Doe')
   email    = models.EmailField('email', max_length=254, default='john_doe@unknow.com')
   phone    = PhoneNumberField(null=False, blank=False, unique=False)
   linkedin = models.URLField('www.linkedin.com')
   address  = models.CharField(max_length=80, default='')
   profile  = models.TextField()

class cv_user_education(models.Model):
   cv_user = models.ForeignKey(cv_user, blank=True, null=True, on_delete=models.CASCADE)
   year   = models.DateField()
   title  = models.CharField(max_length=30)
   school = models.CharField(max_length=50)

   def __str__(self):
      return f"{self.name}"

class cv_user_language(models.Model):
   cv_user = models.ForeignKey(cv_user, blank=True, null=True, on_delete=models.CASCADE)
   title = models.CharField(max_length=20)
   level = models.DecimalField(max_digits=3, decimal_places=0)

   def __str__(self):
      return f"{self.name}"

class cv_user_work_expercience(models.Model):
   cv_user           = models.ForeignKey(cv_user, blank=True, null=True, on_delete=models.CASCADE)
   year              = models.DateField()
   workPlace         = models.CharField(max_length=50)
   city              = models.CharField(max_length=50)
   country           = models.CharField(max_length=50)
   jobTitle          = models.CharField(max_length=50)
   description       = models.TextField(max_length=150)
   professionSkills  = models.TextField(max_length=150)

   def __str__(self):
      return f"{self.name}"