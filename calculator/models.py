from django.db import models

# Create your models here.
class DefaultElementsConcentration(models.Model):
    N = models.DecimalField(max_digits=5, decimal_places=2)
    P2O5 = models.DecimalField(max_digits=5, decimal_places=2)
    K2O = models.DecimalField(max_digits=5, decimal_places=2)
    MgO = models.DecimalField(max_digits=5, decimal_places=2)
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


class ElementsConsuption(models.Model):
    culture = models.CharField(max_length=20, verbose_name='Культура')
    N = models.DecimalField(max_digits=5, decimal_places=2)
    P2O5 = models.DecimalField(max_digits=5, decimal_places=2)
    K2O = models.DecimalField(max_digits=5, decimal_places=2)
    MgO = models.DecimalField(max_digits=5, decimal_places=2)
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
        return self.culture

    class Meta:
        verbose_name = 'Вынос элементов'
        verbose_name_plural = 'Вынос элементов'

class Graph(models.Model):
    graph_img = models.ImageField(upload_to='graphs')
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created_timestamp

    class Meta:
        verbose_name = 'График'
        verbose_name_plural = 'Графики'