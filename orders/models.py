from django.db import models

# Create your models here.
class Order(models.Model):
    email = models.EmailField(max_length=254)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

