from django.db import models

# Create your models here.
class Person(models.Model):
    person_id = models.AutoField
    image = models.ImageField(upload_to="home",default='')

class Contact(models.Model):
    person_id = models.AutoField
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    phno = models.BigIntegerField()
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class User(models.Model):
    user_id = models.AutoField
    user_name = models.CharField(max_length=50)
    user_phno = models.BigIntegerField()
    user_email = models.EmailField(max_length=30)
    user_password = models.CharField(max_length=30,unique=True)


    def __str__(self):
        return self.user_name                

