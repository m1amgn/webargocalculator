from django.contrib import admin
from .models import DefaultElementsConcentration, ElementsConsuption, Graph


# Register your models here.
admin.site.register(DefaultElementsConcentration)
admin.site.register(ElementsConsuption)
admin.site.register(Graph)