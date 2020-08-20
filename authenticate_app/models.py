from django.db import models
from django.conf import settings

# Create your models here.


class jsonContent(models.Model):
    #author = models.ForeignKey('User', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=1000) # 就是json檔案

    def __str__(self):
        return self.title