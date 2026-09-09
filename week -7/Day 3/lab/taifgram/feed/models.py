from django.core.exceptions import ValidationError
from django.db import models


def validate_image(file):
    if not file.name.lower().endswith((".jpg", ".jpeg", ".png")):
        raise ValidationError("Only JPG, JPEG, and PNG images are allowed.")


class Post(models.Model):
    username = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(
        upload_to="posts/",
        validators=[validate_image]
    )
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username