from django.contrib import admin

# Register your models here.

from .models import University, Building, Desk, DeskInstance

#admin.site.register(University)
#Define the admin class
@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    pass

#admin.site.register(Building)
# Define the admin class
@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Desk)
# Define the admin class
@admin.register(Desk)
class DeskAdmin(admin.ModelAdmin):
    pass

#admin.site.register(DeskInstance)
@admin.register(DeskInstance)
class DeskInstanceAdmin(admin.ModelAdmin):
    list_display = ('building', 'desk', 'status')
    list_filter = ('building', 'status')
