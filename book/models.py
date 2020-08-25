from django.db import models

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length = 200)
  bio = models.CharField(max_length = 1000, blank = True)
  image = models.ImageField(upload_to = 'author_images/')
  
  def __str__(self):
    return self.name
    
class Publisher(models.Model):
  name = models.CharField(max_length = 200)
  
  def __str__(self):
    return self.name

class Book(models.Model):
  name = models.CharField(max_length = 200)
  pages = models.IntegerField()
  ratings = models.FloatField()
  authors = models.ManyToManyField(Author, related_name = "books")
  copies = models.IntegerField()
  description = models.CharField(max_length = 1000, blank = True)
  publisher = models.ForeignKey(Publisher, related_name = "books", on_delete = models.CASCADE)
  isbn = models.CharField(max_length = 200, blank = True)
  image = models.ImageField(upload_to = 'book_images/')
  
  def __str__(self):
    return self.name
 