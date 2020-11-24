from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, help_text='This is the Title')
    slug = models.SlugField(max_length=100, unique_for_date='date')
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = ('Post')
        verbose_name_plural = ('Postsd')
        ordering = ('-date',)

    def __str__(self):
        return self.title