from django.db import models

# Create your models here.
# Think of this as a database table which will hold several fields of data that will come from a text field. There will be 3 columns called title, description, and price
# respectively. The parameter for the class is the default Django Model class. 
# py manage.py is the start of every command that will be used with the django project.
# py manage.py makemigrations and py manage.py migrate must be run every time models.py is changed in a component folder to sync the application database with the model class
class Product(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()
    summary = models.TextField(default='This is cool')