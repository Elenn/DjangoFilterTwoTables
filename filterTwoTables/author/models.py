from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Common field

class Book(models.Model):
    title = models.CharField(max_length=100)
    author_email = models.EmailField()  # Common field, but not a ForeignKey