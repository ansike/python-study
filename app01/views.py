import json
from django.shortcuts import render, HttpResponse
from django_redis import get_redis_connection
from django.core import serializers
from django.http import JsonResponse
from .tasks import add

from . import models
# Create your views here.

def index(request):
    return HttpResponse("欢迎使用 app01 index")


def html(request):
    # 根据app的注册顺序，在每个app下的templates目录中寻找
    return render(request, 'index.html')

def redis(request):
    key = 'skey'
    value = 'svalue'
    conn = get_redis_connection('default')
    if conn.get(key) == None:
        conn.set(key, value)
        
    if conn.get(key):
        return HttpResponse('<h1>{0}: {1}</h1>'.format(key, conn.get(key)))
    else:
        return HttpResponse('<h1>没有找到</h1>')

def addUser(request):
    if request.method == 'GET':
        return HttpResponse('<h1>请使用POST增加数据</h1>')
    else:
        # formdata
        # title = request.POST.get("title","")
        # content = request.POST.get("content","")

        # application/json
        data = json.loads(request.body)
        print(data)
        user = models.AUsers.objects.create(title=data['title'], content=data['content'])
        print(user)
        return HttpResponse('新增成功')

def list(request):
    all = models.AUsers.objects.all()
    res = serializers.serialize('json', all)
    return HttpResponse(res)



def async_add(request):
    x = request.GET.get('x')
    y = request.GET.get('y')
    print(x)
    print(y)
    # 调用Celery任务
    result = add(int(x), int(y))
    return JsonResponse({'task_id': result})