from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='img/blog')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 362 or img.width> 251:
            output_size = (362, 251)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='img/recipes')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.pk})

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 362 or img.width> 311:
            output_size = (362, 311)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Carousel(models.Model):
    title_1 = models.CharField(max_length=100)
    title_2 = models.CharField(max_length=100)
    title_3 = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='img')

    def __str__(self):
        return self.title_1

    def get_absolute_url(self):
        return reverse('carousel-detail', kwargs={'pk': self.pk})

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 1920 or img.width> 694:
            output_size = (1920, 694)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog-contact')

    def save(self):
        super().save()

