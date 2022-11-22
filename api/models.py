from django.db import models

# Create your models here.
class Students(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    added_at = models.DateTimeField(auto_now=True)
