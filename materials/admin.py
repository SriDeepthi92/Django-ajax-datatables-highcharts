from django.contrib import admin

from materials.models import compound


class compoundAdmin(admin.ModelAdmin):
    list_display = ('comp_id', 'Fuel_type','zero_carbon_option', 'Fuel_type_rate', 'Zero_carbon_rate', 'green_premium_fuels', 'market' )  # Customize columns in the admin list view
   # Add filters

admin.site.register(compound, compoundAdmin)