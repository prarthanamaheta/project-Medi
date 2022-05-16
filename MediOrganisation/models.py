from django.db import models

from MediUser.models import MediUser


class organisation(models.Model):

    donor_id = models.ForeignKey(MediUser, on_delete=models.CASCADE, related_name='organisation', null=True)
    organisation_name = models.CharField(max_length=50, default='')
    organisation_address = models.CharField(max_length=200)
    organisation_mobile = models.CharField(max_length=10,default='')

    def __str__(self):
        return self.organisation_name
