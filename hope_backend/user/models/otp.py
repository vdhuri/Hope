from django.db  import models

class Otp(models.Model):
    phone=models.TextField()
    otp=models.TextField()