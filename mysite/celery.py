# celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# 设置默认的Django设置模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# 创建Celery实例
app = Celery('mysite')

# 加载配置文件
app.config_from_object('django.conf:settings', namespace='CELERY')

# 自动发现任务
app.autodiscover_tasks()

# celery -A mysite worker -l info