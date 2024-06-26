from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Tag(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

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
    photo = models.ImageField(upload_to='images/')
    price = models.PositiveIntegerField(default=200)

    def __str__(self):
        return self.name

class Sport_list(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(default="@gmail.com")
    photo = models.ImageField(upload_to="images/")
    about_product = models.TextField()
    description = models.FileField(upload_to="descriptions/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

class ReviewsProduct(models.Model):
    reviews_sport = models.ForeignKey(
        Sport_list, on_delete=models.CASCADE, related_name="reviews_product"
    )
    text = models.TextField()
    stars = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.stars}-{self.reviews_sport}"

class Products(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=110)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

