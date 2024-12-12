from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy


class Post(models.Model):
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='Slug')
    title = models.CharField(max_length=255, verbose_name='Title')
    url = models.URLField(unique=True, verbose_name="URL")
    image = models.URLField(default=None, null=True, blank=True, verbose_name="Preview")
    embed = models.URLField(default=None, null=True, blank=True, verbose_name="Embed")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Time create')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Time update')
    streamer = models.ForeignKey('Streamer', on_delete=models.CASCADE, null=True, blank=True, default=None, verbose_name='Streamer')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Author')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('post', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_create']


class Streamer(models.Model):
    user_name = models.CharField(max_length=255, verbose_name="Streamer Name")
    user_id = models.SlugField(default=None, null=True, blank=True, verbose_name="Streamer ID")
    logo = models.URLField(verbose_name="Logo")


class Comment(models.Model):
    text = models.TextField(verbose_name='Text comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')
