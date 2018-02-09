from django.contrib import admin
from .models import molbank
# Register your models here.
#class molAdmin(admin.ModelAdmin):
#	list_display = ('ID',)

admin.site.register(molbank)