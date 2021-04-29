from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(default=None, null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("todo:detail", kwargs={"pk": self.pk})
