from django.contrib import admin

# Register your models here.
from MediDonor.models import Organ, nominee, post, post_like_count

# admin.site.register(common)
admin.site.register(Organ)
admin.site.register(nominee)
admin.site.register(post)
admin.site.register(post_like_count)