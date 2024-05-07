from django.db import models
from accounts.models import UserModel
from django.utils import timezone

class Blog(models.Model):
        title = models.CharField(max_length=200)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        author = models.ForeignKey(UserModel, null=True, blank=True, on_delete=models.CASCADE)

        def __str__(self):
                return self.title
