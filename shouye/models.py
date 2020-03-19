from django.db import models

# Create your models here.
class History(models.Model):
    """b站历史记录存储"""
    title = models.CharField(max_length=200, null=True)  # 标题
    redirect_link = models.CharField(max_length=200, null=True)  # 视频链接
    author = models.CharField(max_length=200, null=True)  # 作者
    view_at = models.DateTimeField(null=True)  # 观看时间
    desc = models.TextField(null=True)  # 描述
    tname = models.CharField(max_length=200, null=True)  # 分类
    pubdate = models.DateTimeField(null=True)  # 发布时间

    class Meta:
        db_table = "History"

    def __str__(self):
        return self.title
