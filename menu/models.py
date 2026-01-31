from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dish(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='dishes/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.title

