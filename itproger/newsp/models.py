from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField('titlee', max_length=50)
    anons = models.CharField('anonss', max_length=250)
    full_text = models.TextField('articlee')
    date = models.DateTimeField('publication date')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f"/news/{self.id}"

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'Some_news'