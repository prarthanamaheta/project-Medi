from django.db import models

from MediUser.models import MediUser


class common(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True


class Organ(common):
    class BloodGroup(models.TextChoices):
        A_positive = 'A+'
        A_negative = 'A-'
        B_positive = 'B+'
        B_negative = 'B-'
        AB_positive = 'AB+'
        AB_negative = 'AB-'
        O_positive = 'O+'
        O_negative = 'O-'

    class Organ_Type(models.TextChoices):
        eye = 'eye'
        kidney = 'kidney'
        heart = 'heart'
        liver = 'liver'
        pancreas = 'pancreas'
        lungus = 'lungus'

    blood_group = models.CharField(max_length=100, choices=BloodGroup.choices, default=BloodGroup.A_positive)
    user_id = models.ForeignKey(MediUser, on_delete=models.CASCADE, related_name='organ', null=True)
    organ_age = models.IntegerField(null=True)
    organ_type = models.CharField(max_length=200, choices=Organ_Type.choices, default=Organ_Type.eye)

    def __str__(self):
        return self.user_id


class nominee(common):
    class Relation(models.TextChoices):
        Father = 'father'
        Mother = 'mother'
        Spouse = 'spouse'
        Brother = 'brother'
        Sister = 'sister'
        Friend = 'friend'

    donor_id = models.OneToOneField(MediUser, on_delete=models.CASCADE, related_name='Nominee', null=True)
    nominee_name = models.CharField(max_length=20)
    nominee_mobile = models.CharField(max_length=10, null=True)
    nominee_email = models.EmailField()
    relation = models.CharField(max_length=10, choices=Relation.choices, default=Relation.Spouse)

    def __str__(self):
        return self.nominee_name


class post(common):
    user_id = models.ForeignKey(MediUser, on_delete=models.CASCADE, related_name='post', null=True)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100, default=" ")
    description = models.CharField(max_length=500, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class post_like_count(models.Model):
    user_id = models.OneToOneField(MediUser, on_delete=models.CASCADE, related_name='post_like_count', null=True)
    post_id = models.OneToOneField(post, on_delete=models.CASCADE, related_name='post_like_count', null=True)
    count_like = models.IntegerField(default=0, editable=False)
    count_dislike = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.post_id
