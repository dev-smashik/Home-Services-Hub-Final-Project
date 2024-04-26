from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class City(models.Model):
    city = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.city

class Status(models.Model):
    status = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.status

class ID_Card(models.Model):
    card = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.card

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.user.first_name

class Service_Man(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    doj = models.DateField(null=True)
    dob = models.DateField(null=True)
    id_type = models.CharField(max_length=100, null=True)
    service_name = models.CharField(max_length=100, null=True)
    experience = models.CharField(max_length=100, null=True)
    id_card = models.FileField(null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.user.first_name



class Service_Category(models.Model):
    category = models.CharField(max_length=30, null=True)
    desc = models.CharField(max_length=100, null=True)
    image = models.FileField(null=True)
    total=models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.category

class Service(models.Model):
    category = models.ForeignKey(Service_Category,on_delete=models.CASCADE,null=True)
    service = models.ForeignKey(Service_Man, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.service.user.first_name

class Contact(models.Model):
    status = models.ForeignKey(Status,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100, null=True)
    message1 = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    def __str__(self):
        return self.name

class Total_Man(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.service.user.first_name

class Order(models.Model):
    report_status = models.CharField(max_length=100, null=True)
    status = models.ForeignKey(Status,on_delete=models.CASCADE,null=True)
    service = models.ForeignKey(Service_Man, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    book_date = models.DateField(null=True)
    book_days = models.CharField(max_length=100, null=True)
    book_hours = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.service.user.first_name+" "+self.customer.user.first_name


class ServiceFeedback(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    friendliness = models.CharField(max_length=100, null=True)
    knowledge = models.CharField(max_length=100, null=True)
    quickness = models.CharField(max_length=100, null=True)
    infuture = models.CharField(max_length=30, null=True)
    suggestion = models.CharField(max_length=300, null=True)
    feedbackdate = models.DateField(null=True)

    def __str__(self):
        return self.id

