from django.db import models
from user.models import UserProfile
from topic.models import Topic

# Create your models here.
class Message(models.Model):
    content = models.CharField(max_length=50,verbose_name='留言内容')
    created_time = models.DateTimeField(verbose_name='留言创建时间',auto_now_add=True)
    parent_message = models.IntegerField(verbose_name='关联的留言ID',default=0)
    publisher = models.ForeignKey(UserProfile)
    topic = models.ForeignKey(Topic)

    class Meta:
        db_table = 'message'