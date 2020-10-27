from django.contrib import admin

# Register your models here.
from user.models import User, D2User

admin.site.register(User)
admin.site.register(D2User)
