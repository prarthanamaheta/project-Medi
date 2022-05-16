from django.db import models


class Transaction(models.Model):
    class status(models.TextChoices):
        process = 'process'
        success = 'success'
        fail = 'fail'

    name = models.CharField(max_length=100)
    amount = models.FloatField()
    payment_id = models.CharField(max_length=100)
    email = models.EmailField(default="")
    status = models.CharField(max_length=200, choices=status.choices, default=status.process)
