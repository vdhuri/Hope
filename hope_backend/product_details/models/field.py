from django.db import models

class Field(models.Model):
    name = models.CharField(max_length=255)
    field_type = models.CharField(max_length=255)
    is_required = models.BooleanField()
    is_disabled = models.BooleanField()

    def __str__(self):
        return self.name
