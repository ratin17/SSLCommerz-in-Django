from django.db import models

# Create your models here.


class Product(models.Model):
    mainimage = models.ImageField(upload_to='shop/images')
    name = models.CharField(max_length=255)
    preview_text = models.TextField(max_length=200, verbose_name='Preview Text')
    detail_text = models.TextField(max_length=1000, verbose_name='Description')
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-price',]
