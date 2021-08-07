from django.contrib import admin
from .models import Culture, VegetationMode, ElementsConcentration, Productivity

# Register your models here.
admin.site.register(Culture)
admin.site.register(VegetationMode)
admin.site.register(ElementsConcentration)
admin.site.register(Productivity)

