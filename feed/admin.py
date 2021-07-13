from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass

# connects Post class with PostAdmin
admin.site.register(Post, PostAdmin)