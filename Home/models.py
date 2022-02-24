from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Owner(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    username=models.CharField(max_length=50,unique = True)
    contact=models.IntegerField()
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Agent(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50,unique = True)
    contact=models.IntegerField()

    def __str__(self):
        return self.name

class Registration(models.Model):
    date=models.DateField(unique = True)
    desc=models.TextField(max_length=500)

    def __str__(self):
        return self.desc

Property_type=(
    ("1","Flat"),
    ("2","Plot"),
    ("3","Villa"),
    ("4","Land"),
    ("5","Residential House"),
    ("6","Penthouse"),
)

class Property(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()
    prop_image=models.FileField(upload_to='media/%Y/%m/%d',null=True,blank=True)
    property_type=models.CharField(max_length=50,choices=Property_type)
    status=models.CharField(max_length=35)
    location=models.CharField(max_length=200,unique = True)
    Owner=models.ForeignKey(Owner,default="ABC",on_delete=models.CASCADE)
    # agent=models.ForeignKey(Agent,default=1,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Property_2(models.Model):
    property=models.ForeignKey(Property,default="ABC",on_delete=models.CASCADE)
    agent=models.ForeignKey(Agent,default="ABC",on_delete=models.CASCADE)

    def __str__(self):
        return self.property.name+" - "+self.agent.name

class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50,unique = True)
    contact=models.IntegerField()
    address=models.TextField()
    image=models.ImageField(upload_to="media/%Y/%m/%d",null=True,blank=True)
    registration=models.ForeignKey(Registration,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    date=models.DateField(auto_now_add=False, null=True,unique = False)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    # owner_id=models.CharField(max_length=5)
    desc=models.CharField(max_length=500,null=True)
    status=models.CharField(max_length=50,null=True)
    owner=models.ForeignKey(Owner,on_delete=models.CASCADE)
    # agent_id=models.ForeignKey(Agent,default=1,on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.desc

class Appointment_2(models.Model):
    owner=models.ForeignKey(Owner,on_delete=models.CASCADE)
    agent=models.ForeignKey(Agent,on_delete=models.CASCADE)

    def __str__(self):
        return self.owner.name+" - "+self.agent.name

class Bill(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    property=models.ForeignKey(Property,on_delete=models.CASCADE)
    owner=models.ForeignKey(Owner,on_delete=models.CASCADE)
    amount=models.IntegerField()
    date=models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.customer.name+" - "+self.owner.name