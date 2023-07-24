from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("欢迎使用")


def html(request):
    # 根据app的注册顺序，在每个app下的templates目录中寻找
    return render(request, 'index.html')
