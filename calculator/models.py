from django.db import models
from webpage.models import Culture

# Create your models here.


class ElementsConsuption(models.Model):
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE, null=True)
    N = models.DecimalField(max_digits=5, decimal_places=2)
    P = models.DecimalField(max_digits=5, decimal_places=2)
    K = models.DecimalField(max_digits=5, decimal_places=2)
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
        return f'{self.culture}'

    class Meta:
        verbose_name = 'Вынос элементов'
        verbose_name_plural = 'Вынос элементов'

class Graph(models.Model):
    graph_img = models.ImageField(upload_to='graphs', blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created_timestamp)

    class Meta:
        verbose_name = 'График'
        verbose_name_plural = 'Графики'