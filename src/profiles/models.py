from django.db import models

class Log(models.Model):
    id = models.AutoField(primary_key=True)
    model_name = models.CharField(null=True, blank=True, max_length=50)
    created = models.DateTimeField(auto_now_add=True)
