from django.db import models

# Create your models here.
class LabDress(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    college_id = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    hostel = models.CharField(max_length=500, null=True, blank=True)
    size = models.CharField(max_length=10, null=True, blank=True)
    taken = models.CharField(max_length=100, null=True, blank=True)
    price = models.CharField(max_length=10, null=True, blank=True)
    added_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name 

class Cycle(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    college_id = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    hostel = models.CharField(max_length=500, null=True, blank=True)
    product_name = models.CharField(max_length=100, null=True, blank=True)
    price = models.CharField(max_length=10, null=True, blank=True)
    payment_type = models.CharField(max_length=100, null=True, blank=True)
    added_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name 