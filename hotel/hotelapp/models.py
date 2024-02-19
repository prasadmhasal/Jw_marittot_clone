from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    dining=models.CharField(max_length=1000,null=True)
    dtype=models.CharField(max_length=1000,null=True)
    descripation= models.CharField(max_length=1000,null=True)
    dtime = models.TimeField(auto_now=True,null=True)
    ntime = models.TimeField(auto_now=True,null=True) 
    day = models.CharField(max_length=1000,null=True) 
    number = models.IntegerField() 
    dresscode=models.CharField(max_length=1000,null=True)
    prebooking=models.IntegerField(null=True)
    image=models.ImageField(upload_to='media',null=True)
    img1=models.ImageField(upload_to='media',null=True)
    img2=models.ImageField(upload_to='media',null=True)
    img3=models.ImageField(upload_to='media',null=True)

class RoomProduct(models.Model):
    room=models.CharField(max_length=1000,null=True)
    capacity=models.CharField(max_length=1000,null=True)
    desc=models.CharField(max_length=1000,null=True)
    view=models.CharField(max_length=1000,null=True)
    caption=models.CharField(max_length=1000,null=True)
    time = models.TimeField(auto_now=True,null=True)
    time1 = models.TimeField(auto_now=True,null=True)
    price = models.FloatField(max_length=1000,null=True)  
    beds_bedding = models.CharField(max_length=1000,null=True)
    food_beverages = models.CharField(max_length=1000,null=True)
    entertainment  = models.CharField(max_length=1000,null=True)
    bath_bathroom_features = models.CharField(max_length=1000,null=True)
    kitchen_features = models.CharField(max_length=1000,null=True)
    room_features = models.CharField(max_length=1000,null=True)
    accessible_features = models.CharField(max_length=1000,null=True)
    furniture_furnishings = models.CharField(max_length=1000,null=True)
    internet_phones = models.CharField(max_length=1000,null=True)
    hospitality_services = models.CharField(max_length=1000,null=True)
    image=models.ImageField(upload_to=1000,null=True)
    img1=models.ImageField(upload_to='media',null=True)
    img2=models.ImageField(upload_to='media',null=True)
    img3=models.ImageField(upload_to='media',null=True)

class RoomOffer(models.Model):
    room=models.CharField(max_length=1000,null=True)
    capacity=models.CharField(max_length=1000,null=True)
    desc=models.CharField(max_length=1000,null=True)
    caption=models.CharField(max_length=1000,null=True)
    startdate = models.CharField(max_length=1000,null=True)
    enddate = models.CharField(max_length=1000,null=True)
    price = models.FloatField(max_length=1000,null=True)  
    include = models.CharField(max_length=1000,null=True)
    needknow = models.CharField(max_length=1000,null=True)
    image=models.ImageField(upload_to='media',null=True)
    img1=models.ImageField(upload_to='media',null=True)
    img2=models.ImageField(upload_to='media',null=True)
    img3=models.ImageField(upload_to='media',null=True)


class DiningBooking(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    restaurant = models.CharField(max_length=100,null=True)
    time = models.TimeField(auto_now=True,null=True)
    adult = models.CharField(max_length=100,null=True)
    date = models.DateField(max_length=100,null=True)
    children = models.CharField(max_length=100,null=True)
    prebooking=models.FloatField()
    title=models.CharField(max_length=100,null=True)
    first_name=models.CharField(max_length=100,null=True)
    last_name=models.CharField(max_length=100,null=True)
    cnumber = models.CharField(max_length=100,null=True) 
    number = models.IntegerField() 
    email =models.CharField(max_length=100 , null=True)
    note=models.CharField(max_length=1000,null=True)




def __str__(self):
        return self.dish