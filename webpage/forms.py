from django import forms
from .models import Culture, VegetationMode


class CalculateForms(forms.Form):
    culture = forms.ModelChoiceField(label='Культура*', queryset=Culture.objects.all())
    climat_zone = forms.ModelChoiceField(label='Район*', queryset=VegetationMode.objects.all())
    quantity_of_water = forms.DecimalField(label='Среднее количество осадков за период вегетации, мм*', max_digits=5, decimal_places=2, min_value=0)
    temperature = forms.DecimalField(label='Средняя температура за период вегетации, С*', max_digits=5, decimal_places=2, min_value=0)
    productivity = forms.DecimalField(label='Планируемая урожайность, ц/га*', max_digits=5, decimal_places=2, min_value=0)
    N = forms.DecimalField(label='Концентрация азота в почве, мг/кг', max_digits=6, decimal_places=3, min_value=0, required=False)
    P = forms.DecimalField(label='Концентрация фосфора в почве, мг/кг', max_digits=6, decimal_places=3, min_value=0, required=False)
    K = forms.DecimalField(label='Концентрация калия в почве, мг/кг', max_digits=6, decimal_places=3, min_value=0, required=False)
    Mg = forms.DecimalField(label='Концентрация магния в почве, мг/кг', max_digits=6, decimal_places=3, min_value=0, required=False)
    S = forms.DecimalField(label='Концентрация серы в почве, мг/кг', max_digits=6, decimal_places=3, min_value=0, required=False)
    Ca = forms.DecimalField(label='Концентрация кальция в почве, мг/кг', max_digits=6, decimal_places=3, min_value=0, required=False)
    Fe = forms.DecimalField(label='Концентрация железа в почве, мг/кг', max_digits=6, decimal_places=3, min_value=0, required=False)
    Mn = forms.DecimalField(label='Концентрация марганца в почве, мг/кг', max_digits=6, decimal_places=3, min_value=0, required=False)
    Zn = forms.DecimalField(label='Концентрация цинка в почве, мг/кг', max_digits=6, decimal_places=3, min_value=0, required=False)
    Cu = forms.DecimalField(label='Концентрация меди в почве, мг/кг', max_digits=6, decimal_places=3, min_value=0, required=False)
    B = forms.DecimalField(label='Концентрация бора в почве, мг/кг', max_digits=6, decimal_places=3, min_value=0, required=False)
    Mo = forms.DecimalField(label='Концентрация молибдена в почве, мг/кг', max_digits=6, decimal_places=3, min_value=0, required=False)
    Co = forms.DecimalField(label='Концентрация кобальта в почве, мг/кг', max_digits=6, decimal_places=3, min_value=0, required=False)
    Ni = forms.DecimalField(label='Концентрация никеля в почве, мг/кг', max_digits=6, decimal_places=3, min_value=0, required=False)
    Se = forms.DecimalField(label='Концентрация селена в почве, мг/кг', max_digits=6, decimal_places=3, min_value=0, required=False)
