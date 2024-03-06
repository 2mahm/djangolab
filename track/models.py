from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class productd(models.Model):
    name = models.CharField(max_length=15)
    price = models.IntegerField(default=15)
    @classmethod
    def get_products(cls):
        return cls.objects.all()


