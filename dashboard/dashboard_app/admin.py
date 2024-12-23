from django.contrib import admin
from .models import State, City, Property

# Register State model
@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Display id and name in the admin list view
    search_fields = ('name',)  # Enable search by name


# Register City model
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'state')  # Display id, name, and state in the admin list view
    search_fields = ('name',)  # Enable search by name
    list_filter = ('state',)  # Filter cities by state


# Register Property model
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('property_id', 'property_name', 'city', 'owner_name')  # Display fields in list view
    search_fields = ('property_name', 'owner_name', 'city__name')  # Enable search by name and city
    list_filter = ('city',)  # Filter properties by city
