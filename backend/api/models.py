from django.db import models

class News(models.Model):
    date = models.DateField() 
    news = models.JSONField()  

    def __str__(self):
        return self.date
