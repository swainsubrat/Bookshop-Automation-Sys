from django.db import models

# Create your models here.
class Stock(models.Model):
    def __str__(self):
        return self.book_name
    book_name = models.CharField(max_length=30)
    book_cat = models.CharField(max_length=30)
    book_auth = models.CharField(max_length=30)
    book_pub =models.CharField(max_length=30)
    book_price = models.FloatField()
    book_qty = models.IntegerField()
    shelf_no = models.IntegerField(default=5)
    objects = models.Manager()
