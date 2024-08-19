from django.db import models
from django.contrib.auth.models import User
class app(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    image = models.ImageField(upload_to="images")
    category_name = models.CharField(max_length=100)
    sub_category_name = models.CharField(max_length=100)
    point=models.IntegerField(default=1)

    def __str__(self):
        return self.name

class user_task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_point = models.IntegerField(default=10)

    def __str__(self):
        return self.user.username