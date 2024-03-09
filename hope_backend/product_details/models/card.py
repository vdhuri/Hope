from django.db import models
from .template import Template
from .field_value import FieldValue

class Card(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    values = models.ManyToManyField(FieldValue)

    def __str__(self):
        return f"{self.template.name} - Card {self.id}"
