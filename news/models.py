from django.db import models
from django.utils import timezone

# Create your models here.
# news/models.py


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField('शीर्षक', max_length=200)
    content = models.TextField('सामग्री')
    publication_date = models.DateTimeField('प्रकाशन मिति', default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    # हामी यसलाई पछि थप्नेछौं, तर अहिलेको लागि यो सरल राखौं।
    # image = models.ImageField('तस्वीर', upload_to='images/')

       # --- THIS IS THE NEW LINE YOU ARE ADDING ---
    image = models.ImageField('तस्वीर', upload_to='images/', blank=True, null=True)
    # -------------------------------------------

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publication_date'] # नयाँ समाचारलाई माथि देखाउन