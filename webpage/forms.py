from django import forms
from .models import Culture, VegetationMode


class CalculateForms(forms.Form):
    culture = forms.ModelMultipleChoiceField(queryset=Culture.objects.all())
    climat_zone = forms.ModelMultipleChoiceField(queryset=VegetationMode.objects.all())
    # quantity_of_water = forms.DecimalField(max_digits=5, decimal_places=2, min_value=0, required=False)
    # temperature = forms.DecimalField(max_digits=5, decimal_places=2, min_value=0, required=False)
    productivity = forms.DecimalField(max_digits=5, decimal_places=2, min_value=0, required=False)
    N = forms.DecimalField(max_digits=5, decimal_places=2, min_value=0, required=False)
    P2O5 = forms.DecimalField(max_digits=5, decimal_places=2, min_value=0, required=False)
    K2O = forms.DecimalField(max_digits=5, decimal_places=2, min_value=0, required=False)
    Mg = forms.DecimalField(max_digits=5, decimal_places=2, min_value=0, required=False)
    S = forms.DecimalField(max_digits=5, decimal_places=2, min_value=0, required=False)
    Ca = forms.DecimalField(max_digits=5, decimal_places=2, min_value=0, required=False)
    Fe = forms.DecimalField(max_digits=5, decimal_places=2, min_value=0, required=False)
    Mn = forms.DecimalField(max_digits=5, decimal_places=2, min_value=0, required=False)
    Zn = forms.DecimalField(max_digits=5, decimal_places=2, min_value=0, required=False)
    Cu = forms.DecimalField(max_digits=5, decimal_places=2, min_value=0, required=False)
    B = forms.DecimalField(max_digits=5, decimal_places=2, min_value=0, required=False)
    Mo = forms.DecimalField(max_digits=5, decimal_places=2, min_value=0, required=False)
    Co = forms.DecimalField(max_digits=5, decimal_places=2, min_value=0, required=False)
    Se = forms.DecimalField(max_digits=5, decimal_places=2, min_value=0, required=False)
