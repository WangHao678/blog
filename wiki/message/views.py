import json

from django.http import JsonResponse
from django.shortcuts import render

from message.models import Message
from tools.logging_check import logging_check

# Create your views here.
from topic.models import Topic


@logging_check('POST')
def messages(request,topic_id):
    if request.method == 'POST':
        #发表留言/回复
        json_str = request.body
        json_obj = json.loads(json_str)
        content = json_obj.get('content')
        parent_id = json_obj.get('parent_id',0)
        #TODO 参数检查

        #检查topic是否存在
        try:
            topic = Topic.objects.get(id=topic_id)
        except Exception as e:
            result = {'code':40101,'error':'No topic'}
            return JsonResponse(result)
        #第一种方案 可以直接对外键属性赋值 对象
        Message.objects.create(content=content,parent_message=parent_id,
                               publisher=request.user,topic=topic)
        #第二种方案 用外键 赋值给 外键字段名
        # Message.objects.create(content=content, parent_message=parent_id,
        #                        publisher_id=request.user.username,topic_id=topic_id)
        return JsonResponse({'code':200})

    if request.method == 'GET':
        #/v1/messages/topic_id
        all_m =Message.objects.filter(topic_id=int(topic_id))
        all_list = []
        for m in all_m:
            d = {}
            d['id'] = m.id
            d['content'] = m.content
            d['parent_message'] = m.parent_message
            d['publisher'] = m.publisher.username
            d['topic'] = m.topic.id
            all_list.append(d)
        return JsonResponse({'code':200,'data':all_list})


























