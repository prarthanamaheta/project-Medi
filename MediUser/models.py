from django.contrib.auth import get_user_model

from django.contrib.auth.models import User
from django.db import models


class MediUser(models.Model):
    class UserType(models.TextChoices):
        donor = 'donor'
        donee = 'donee'

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    get_user_model()
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    profile_image = models.ImageField(upload_to='images', null=True, blank=True, name='Profile Image')
    user_type = models.CharField(max_length=10, choices=UserType.choices, default=UserType.donor)

    USERNAME_FIELD = ('username')

    def __str__(self):
        return self.username

    class Meta:
        order_with_respect_to = 'user'


from MediDonor.models import Organ


class Donation(models.Model):
    user_id = models.ForeignKey(MediUser, on_delete=models.CASCADE, related_name='Donation', null=True)

    from MediOrganisation.models import organisation

    organisation_id = models.ForeignKey(organisation, on_delete=models.CASCADE, related_name='Donation', null=True)
    organ_id = models.ForeignKey(Organ, on_delete=models.CASCADE, related_name='Donation', null=True)

    def __str__(self):
        return self.user_id
