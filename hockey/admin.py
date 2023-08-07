from django.contrib import admin
from .models import player
# Register your models here.
class sportAdmin(admin.ModelAdmin):
    list_display = ['name','age','city']
admin.site.register(player,sportAdmin)
