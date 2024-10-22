from django.contrib import admin
from services.models import user

class usersAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','mail','contact','password')


admin.site.register(user,usersAdmin)
