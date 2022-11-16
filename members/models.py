from django.db import models

# Create your models here.
class Members(models.Model):
	firstname = models.CharField(max_length=255)
	lastname = models.CharField(max_length=255)

class Comments(models.Model):
	name = models.CharField(max_length=255)
	text = models.TextField(max_length=511)