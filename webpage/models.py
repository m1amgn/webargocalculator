from django.db import models

# Create your models here.


class Culture(models.Model):
    culture = models.CharField(max_length=20, verbose_name='Культура')

    def __str__(self):
        return self.culture

    class Meta:
        verbose_name = 'Культура'
        verbose_name_plural = 'Культуры'

class VegetationMode(models.Model):
    climat_zone = models.CharField(max_length=50, verbose_name='Климатическая зона', default='')


    def __str__(self):
        return self.climat_zone

    class Meta:
        verbose_name = 'Климатическая зона'
        verbose_name_plural = 'Климатические зоны'

class Productivity(models.Model):
    climat_zone = models.ForeignKey(VegetationMode, on_delete=models.CASCADE, null=True)
    productivity = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Урожайность')

    def __str__(self):
        return f'{self.climat_zone}'

    class Meta:
        verbose_name = 'Урожайность'
        verbose_name_plural = 'Урожайность'

class ElementsConcentration(models.Model):
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE, null=True)
    climat_zone = models.ForeignKey(VegetationMode, on_delete=models.CASCADE, null=True)
    N = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    P2O5 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    K2O = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Mg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    S = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Ca = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Fe = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Mn = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Zn = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Cu = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    B = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Mo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Co = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Se = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    quantity_of_water = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    productivity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created_timestamp)

    class Meta:
        verbose_name = 'Данные из формы'
        verbose_name_plural = 'Данные из формы'

class DefaultElementsConcentration(models.Model):
    N = models.DecimalField(max_digits=5, decimal_places=2)
    P2O5 = models.DecimalField(max_digits=5, decimal_places=2)
    K2O = models.DecimalField(max_digits=5, decimal_places=2)
    Mg = models.DecimalField(max_digits=5, decimal_places=2)
    S = models.DecimalField(max_digits=5, decimal_places=2)
    Ca = models.DecimalField(max_digits=5, decimal_places=2)
    Fe = models.DecimalField(max_digits=5, decimal_places=2)
    Mn = models.DecimalField(max_digits=5, decimal_places=2)
    Zn = models.DecimalField(max_digits=5, decimal_places=2)
    Cu = models.DecimalField(max_digits=5, decimal_places=2)
    B = models.DecimalField(max_digits=5, decimal_places=2)
    Mo = models.DecimalField(max_digits=5, decimal_places=2)
    Co = models.DecimalField(max_digits=5, decimal_places=2)
    Se = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'Концентрация элементов по умолчанию'

    class Meta:
        verbose_name = 'Содержание элементов по умолчанию'
        verbose_name_plural = 'Содержание элементов по умолчанию'