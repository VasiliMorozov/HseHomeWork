from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.IntegerField()

    def get_absolute_url(self):
        return reverse('products:detail', args=(self.pk,))
