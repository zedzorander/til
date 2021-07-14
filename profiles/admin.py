from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    pass

# connects Profile class with ProfileAdmin
admin.site.register(Profile, ProfileAdmin)