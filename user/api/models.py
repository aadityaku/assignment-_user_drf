from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    task=models.TextField(max_length=200)
    status=models.BooleanField(default=False)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.task