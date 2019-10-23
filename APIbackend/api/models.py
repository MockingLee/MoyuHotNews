from django.db import models


# Create your models here.

class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=70)
    url = models.CharField(max_length=300)
    # img = models.CharField('img src', max_length=300)
    site_type = models.CharField(max_length=7, blank=True)
    create_time = models.DateTimeField(auto_now=True)
    rank = models.IntegerField(blank=False)
    generation = models.IntegerField(blank=False)

    def __str__(self):
        return '%s_%s' % (self.site_type, self.title)
