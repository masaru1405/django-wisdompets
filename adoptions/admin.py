from django.contrib import admin

from .models import Pet

#admin.site.register(Pet)

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
   list_display = ['name', 'species', 'breed', 'age', 'sex']