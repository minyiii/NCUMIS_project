from django.db import models
from django.conf import settings
import uuid

# Create your models here.

class jsonContent(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    upload = models.FileField(upload_to='uploads/') # md檔
    # https://www.cnblogs.com/huchong/p/7894860.html
    # content = models.CharField(max_length=1500, blank=True, null=True) # 就是json檔案(若長度僅設定最多1000，很可能會無法讀取json檔案(因為自數可能超過))
    content = models.FileField(upload_to='uploads_json/') # json檔
    # https://miny.app/u012111465
    # content = JSONField(default=None)

    def __str__(self):
        return self.title