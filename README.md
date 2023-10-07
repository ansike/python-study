# 仅作 django 学习记录

### 1. 基本的安装启动流程
```shell
# 安装django
pip install django
# pip3 install django

# 查看django版本
python3 -m django --version
# 4.2.5

# 初始化django项目
django-admin.exe startproject xxx
# 初始化一个app
python.exe .\manage.py startapp app01
# 注册当前app到django中
# mysite/settings.py
#INSTALLED_APPS = [
#    ***
#    'app01.apps.App01Config' # 注册app
#]

# 配置视图
#mysite/urls.py
#from app01 import views
#urlpatterns = [
#    path('', views.index),
#]

#app01/views.py
#from django.shortcuts import render, HttpResponse
#def index(request):
#    return HttpResponse("欢迎使用")

# 启动服务
python.exe .\manage.py runserver 8000 # windows
python3 manage.py runserver 8000 # mac
```

### 2. 加载html输出视图



### 3. 连接redis mysql celery



### 4. 使用




# FAQ
1. You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.

Run 'python manage.py migrate' to apply them.

