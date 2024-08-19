from django.contrib.auth.models import User
from django.db import models


class PageRequest(models.Model):
    class Status(models.TextChoices):
        PENDING = "P", "Pending"
        GENERATING = "G", "Generating"
        READY = "R", "Ready"
        ERROR = "E", "Error"

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=128)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.PENDING
    )
    error_msg = models.CharField(max_length=128, blank=True, null=True)
    pdf_file = models.FileField(upload_to=f"pdfs", blank=True, null=True)

    def __str__(self):
        return f"{self.pk} ({self.url})"
