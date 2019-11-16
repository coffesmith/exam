from django.db import models

# Create your models here.
class Seed(model.Model):
    fake_data = models.TextField()