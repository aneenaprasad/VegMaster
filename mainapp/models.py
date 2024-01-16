from django.db import models

class Register(models.Model):
    user_name = models.CharField(max_length=20)
    user_age = models.IntegerField()
    user_contactno= models.IntegerField()
    user_email= models.EmailField()
    user_password= models.CharField(max_length=20)
class Category(models.Model):
    category =models.CharField(max_length=20)
    category_img=models.ImageField(upload_to='catimg',default='null.jpg')
class Product(models.Model):
    Category=models.ForeignKey(Category,on_delete=models.DO_NOTHING,null=True,blank=True)
    product_image=models.ImageField(upload_to='products',default='null.jpg')
    product_name=models.CharField(max_length=50)
    product_price=models.IntegerField()
class Blog(models.Model):
    b_image=models.ImageField(upload_to='blogimage',default='null.jpg')
    b_name=models.CharField(max_length=20)
    b_date=models.DateField()
    b_enterblog=models.CharField(max_length=30)
class Wishlist(models.Model):
    wishproduct=models.ForeignKey(Product,on_delete=models.DO_NOTHING,null=True,blank=True)
    wishuser=models.ForeignKey(Register,on_delete=models.DO_NOTHING,null=True,blank=True)
    date=models.DateField(auto_now_add=True)
class Cart(models.Model):
    cartproduct=models.ForeignKey(Product,on_delete=models.DO_NOTHING,null=True,blank=True)
    cartuser=models.ForeignKey(Register,on_delete=models.DO_NOTHING,null=True,blank=True)
    product_size=models.CharField(max_length=30)
    product_quantity=models.IntegerField()
    totalsize=models.IntegerField(default=0)
class Comment(models.Model):
    datee=models.DateField()
    addcomplain=models.CharField(max_length=30)


