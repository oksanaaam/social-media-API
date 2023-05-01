import os
import uuid

from django.conf import settings
from django.db import models
from django.utils.text import slugify


def profile_picture_file_path(user, filename):
    _, extension = os.path.splitext(filename)

    filename = f"{slugify(user.id)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/posts", filename)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to=profile_picture_file_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"author: {self.author}, content: {self.content}"
            f" created_at: {self.created_at.strftime('%Y-%m-%d %H:%M')}"
        )
