from django.db import models
from webpage.models import Culture

# Create your models here.


class ElementsConsuption(models.Model):
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE, null=True)
    N = models.DecimalField(max_digits=5, decimal_places=3, default=0)
    P = models.DecimalField(max_digits=5, decimal_places=3, default=0)
    K = models.DecimalField(max_digits=5, decimal_places=3, default=0)
    Mg = models.DecimalField(max_digits=5, decimal_places=3, default=0)
    S = models.DecimalField(max_digits=5, decimal_places=3, default=0)
    Ca = models.DecimalField(max_digits=5, decimal_places=3, default=0)
    Fe = models.DecimalField(max_digits=5, decimal_places=3, default=0)
    Mn = models.DecimalField(max_digits=5, decimal_places=3, default=0)
    Zn = models.DecimalField(max_digits=5, decimal_places=3, default=0)
    Cu = models.DecimalField(max_digits=5, decimal_places=3, default=0)
    B = models.DecimalField(max_digits=5, decimal_places=3, default=0)
    Mo = models.DecimalField(max_digits=5, decimal_places=3, default=0)
    Co = models.DecimalField(max_digits=5, decimal_places=3, default=0)
    Ni = models.DecimalField(max_digits=5, decimal_places=3, default=0)
    Se = models.DecimalField(max_digits=5, decimal_places=3, default=0)

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