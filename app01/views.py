from django.shortcuts import render, HttpResponse
from django_redis import get_redis_connection

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
