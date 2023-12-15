from django.db import models

class Bike(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='bike_photos/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    purchase_date = models.DateField()

    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        ordering = ['-price']