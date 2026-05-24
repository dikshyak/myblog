from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Post(models.Model):
    title     = models.CharField(max_length=200)
    slug      = models.SlugField(unique=True, blank=True)
    excerpt   = models.TextField(blank=True)
    content   = models.TextField()
    image     = models.ImageField(upload_to='posts/', blank=True, null=True)
    author    = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    created   = models.DateTimeField(auto_now_add=True)
    updated   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created']