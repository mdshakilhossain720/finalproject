from django.db import models
from django.contrib.auth.models import User

# Create your models here.

DIVISION_CHOOSE=(
    ('Dhaka','Dhaka'),
    ('Rangpur','Rangpur'),
    ('Rajshi','Rajshi'),
    ('Barishal','Barishal'),
    ('sylhet','Sylhet'),
    ('Khulna','Khulna'),
    
)

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    division=models.CharField(choices=DIVISION_CHOOSE,max_length=200)
    district=models.CharField(max_length=200)
    thana=models.CharField(max_length=50)
    villageroad=models.CharField(max_length=50)
    zipcode=models.IntegerField()

    def __str__(self):
        return str(self.id)
    


CATAGORY =(
        ('L','Lengea'),
        ('S','sari'),
        ('GP','Gents Pant'),
        ('BK','Borkha'),
        ('BF','Baby Fashion'),


    )

class Product(models.Model):
        title=models.CharField(max_length=100)
        selling_prices=models.FloatField()
        discount=models.FloatField()
        description=models.TextField(max_length=300)
        brand=models.CharField(max_length=100)
        category=models.CharField(choices=CATAGORY,max_length=50)
        product_image=models.ImageField(upload_to='MyImage')


        def __str__(self):
            return str(self.id)
        

class Cart(models.Model):
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     product=models.ForeignKey(Product,on_delete=models.CASCADE)
     quanity=models.PositiveIntegerField()

     def __str__(self):
         return str(self.name)
     

STATUS_CHOOSE=(
     ('Accepted','Accepted'),
     ('Packed','Packed'),
     ('On The Way','On The Way'),
     ('Delivery','Delivery'),
     ('Cancell','Cancell'),

)


class OrderPlace(models.Model):
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
     product=models.ForeignKey(Product,on_delete=models.CASCADE)
     quantity=models.PositiveBigIntegerField(default=1)
     oeder_date=models.DateTimeField(auto_now_add=True)
     status=models.CharField(max_length=50,choices=STATUS_CHOOSE,default='Pending')
     
     
        

        
    

    
