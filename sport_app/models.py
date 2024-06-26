from django.db import models

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.text} - {self.author}"

class YTVideo(models.Model):
    video = models.URLField()

    def __str__(self):
        return self.video

class Topfive(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='/images/')
    price = models.PositiveIntegerField(default=200)

    def __str__(self):
        return self.name