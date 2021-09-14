from django.db import models
from datetime import datetime

class Customer(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    current_balance = models.IntegerField()


class Transaction(models.Model):
    From = models.CharField(max_length=20, null=True)
    To = models.CharField(max_length=20, null=True)
    transaction_amt = models.IntegerField()
    datetime = models.DateTimeField(default=datetime.now, blank=True)
