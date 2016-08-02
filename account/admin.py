from django.contrib import admin
from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk','username', 'email', 'time_create')
    list_filter = ['time_create']
    search_fields = ['username', 'email']

admin.site.register(User, UserAdmin)