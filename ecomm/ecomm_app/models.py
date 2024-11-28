from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    CAT=((1,'MOBILE'),(2,'SHOES'),(3,'CLOTHES'))
    name=models.CharField(max_length=50,verbose_name='Product Name')
    price=models.FloatField(verbose_name='Product Price')
    pdetails=models.CharField(max_length=100)
    cat=models.IntegerField(verbose_name='Product Category',choices=CAT)
    is_active=models.BooleanField(default=True,verbose_name='Available')
    pimage=models.ImageField(upload_to='image')


    def __str__(self):
        return self.name
class cart(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column="pid")
    qty=models.IntegerField(default=1)
class order(models.Model):
    order_id=models.CharField(max_length=50)
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column="pid")
    qty=models.IntegerField(default=1)