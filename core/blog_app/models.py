from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
    """
    this is  a class to define posts for blog app
    """
    author = models.ForeignKey('accounts_app.Profile', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=300)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, allow_unicode=True, null=True, blank=True)

    class Meta:
        ordering = ['-created_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_app:post-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Category(models.Model):
    """
    this is  a class to define categories for posts in blog app
    """
    name = models.CharField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
