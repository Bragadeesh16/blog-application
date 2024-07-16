from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Post(models.Model):
    Title = models.CharField(max_length=100)
    Content = models.TextField()
    Author = models.ForeignKey(User,on_delete=models.CASCADE)
    Published_Date = models.DateTimeField(auto_now=True)
    slug = models.SlugField( blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Title

class Comment(models.Model):
    Post = models.ForeignKey(Post,on_delete=models.CASCADE)
    Author = models.ForeignKey(User,on_delete=models.CASCADE)
    Content = models.TextField()
    Created_date = models.DateTimeField(auto_now=True)

