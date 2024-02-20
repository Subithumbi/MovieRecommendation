
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    # slug=models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name='category'
        verbose_name='categories'

    def get_url(self):
        return reverse('moviepostapp:movies_by_category', args=[str(self.id)])
    def __str__(self):
        return self.name
class Movie(models.Model):
    title = models.CharField(max_length=255)
    # slug=models.SlugField(max_length=255,unique=True)
    poster = models.ImageField(upload_to='movie_posters/')
    description = models.TextField(blank=True)
    release_date = models.DateField()
    actors = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    trailer_link = models.URLField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('moviepostapp:movieCatdetail',args=[self.category.id,self.id])



    class Meta:
        ordering = ('title',)
        verbose_name='movie'
        verbose_name='movies'

    def __str__(self):
        return  '{}'.format(self.title)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


