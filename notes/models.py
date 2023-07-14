from django.db import models

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateField(auto_now_add= True)
    
class Contacts(models.Model):
    contact_name = models.CharField(max_length=200)
    Contact_num = models.IntegerField()
    created = models.DateField(auto_now_add= True)