from django.db import models
from django.contrib.auth.models import User


class Mailer(models.Model):
    content = models.TextField()
    subject = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    from_field = models.EmailField()
    
