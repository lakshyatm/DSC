from django.db import models

# Create your models here.

class Kitty(models.Model):
    event_name = models.CharField(max_length=50)
    person1 = models.CharField(max_length=100)
    person1_email = models.CharField(max_length=100)
    person2 = models.CharField(max_length=100)



class Expense(models.Model):
    paid_person = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=20,decimal_places=8)
    split_equ_all = models.BooleanField(default=True)
    split_diff = models.BooleanField(default=False)
    exp_name = models.CharField(max_length=100)
    date= models.DateField()
