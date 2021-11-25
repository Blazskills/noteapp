from django.contrib import admin
from .models import Colors, Note, Priority, User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('email','first_name', 'last_name', 'is_superuser', 'is_staff')
  
    list_filter = ['created']
    search_fields = ['first_name']

admin.site.register(User, UserAdmin)
admin.site.register(Note)
admin.site.register(Colors)
admin.site.register(Priority)


