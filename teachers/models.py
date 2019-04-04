from django.db import models

# Create your models here.

class Teacher(models.Model):
    name_tea = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name_tea

class Object(models.Model):
    teach = models.ForeignKey(Teacher, on_delete=models.CASCADE, max_length=100)
    name_obj = models.CharField(max_length=100, null=True, blank=True)
    credit = models.CharField(max_length=10, null=True, blank=True)
    #describe = models.TextField()

    def __str__(self):
        return self.name_obj
