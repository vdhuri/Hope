from django.db import models
from .field import Field

class FieldValue(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    text = models.TextField()
    file = models.FileField(upload_to='field_values/', null=True, blank=True)

    def __str__(self):
        return f"{self.field.name} - {self.text[:50]}"
