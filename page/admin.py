from django.contrib import admin
from .models import Property
# Register your models here.

admin.site.site_header = "Rental System Admin"
admin.site.site_title = "Rental System Admin Area"
admin.site.index_title = "Welcome to Rental System admin area" 

class PropetyAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'area', 'property_type')
    # list_display_links = ('title',)
    search_fields = ('title',)
    # fields = ('title', 'description','location', 'price', 'area', 'type_property') use to show needed fields
    list_filter = ('property_type',)




 

admin.site.register(Property, PropetyAdmin)

