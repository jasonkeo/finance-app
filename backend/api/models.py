import models

class News(models.Model):
    date = models.TextField() 
    news = models.TextField()  

    def __str__(self):
        return self.date
