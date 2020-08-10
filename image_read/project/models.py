from __future__ import unicode_literals
# from djongo import models
from django.db import  models
from django.urls import reverse

# Create your models here.
class image_extract(models.Model):
    seat_no = models.IntegerField(primary_key=True,null=False)
    image = models.ImageField()
    name = models.CharField(max_length=250,blank=True)
    mother_name = models.CharField(max_length=250,blank=True)
    college_name = models.CharField(max_length=250,blank=True)
    center_no = models.IntegerField(blank=True)
    total_marks = models.IntegerField(blank=True)

    def __str__(self):
        return str(self.seat_no)

    def get_absolute_url(self):
        return reverse("project:image_detail",kwargs={'pk':self.pk})