from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from .models import Category,Movie

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]
    # prepopulated_fields = {'id': ('name',)}
admin.site.register(Category,CategoryAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title','release_date']
admin.site.register(Movie,MovieAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ['user']

    def __str__(self):
        return self.user