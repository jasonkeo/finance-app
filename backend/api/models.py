from django.db import models

class News(models.Model):
    date = models.TextField() 
    news = models.JSONField()  
    index = models.JSONField() 
    analysis = models.TextField()
    def __str__(self):
        return self.date

