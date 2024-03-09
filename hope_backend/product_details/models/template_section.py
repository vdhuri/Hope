from django.db import models
from .template import Template

class TemplateSection(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    plan_type = models.CharField(max_length=255)  # Add the plan_type field
    fields = models.ManyToManyField('Field')  # Assuming 'Field' is the name of your Field model

    def __str__(self):
        return f"{self.template.name} - {self.plan_type}"
