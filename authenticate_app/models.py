from django.db import models
from django.conf import settings
#from django.contrib.postgres.fields import JSONField

# Create your models here.


class jsonContent(models.Model):
    #author = models.ForeignKey('User', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    upload = models.FileField(upload_to='uploads/')
    # https://www.cnblogs.com/huchong/p/7894860.html
    content = models.CharField(max_length=1500, blank=True, null=True)
    # https://miny.app/u012111465
    #content = JSONField(default=None)
    
    

    def __str__(self):
        return self.title



