from django.db import models

# Create your models here.
class Content(models.Model):
    page = models.IntegerField()
    title = models.CharField(max_length=50)
    image = models.ImageField()
    info = models.TextField()
    download = models.FileField(upload_to='document/s', blank=True)
    
    def __str__(self):
        return self.title
    
class About(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=600)
    
    def __str__(self):
        return self.title
