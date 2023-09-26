from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True, auto_now=False, verbose_name="Date")
    slug = models.SlugField(unique=True, blank=True, null=True)

@receiver(pre_save, sender=Article)
def set_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

