import os
from datetime import timedelta
from celery import Celery, platforms
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coc.settings')

app = Celery('coc')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
platforms.C_FORCE_ROOT = True

app.conf.update(
    CELERYBEAT_SCHEDULE={
        'sync_clan_members': {
            # 每天凌晨零点五分录入部落成员数据
            'task': 'v1.tasks.sync_clan_members',
            'schedule': crontab(hour=0, minute=5),
        },
        'sync_users_info': {
            # 每天凌晨零点十分录入当前成员的统计数据
            'task': 'v1.tasks.sync_users_info',
            'schedule': crontab(hour=0, minutes=10),
        },
        'sync_attack_log': {
            'task': 'v1.tasks.sync_attack_log',
            # 每周一下午三点半录入突袭进攻数据
            'schedule': crontab(hour=15,minutes=30, day_of_week='mon'),
        },
        'sync_calculate': {
            'task': 'v1.tasks.sync_calculate',
            # 每月 1 号凌晨计算上月的贡献数据
            'schedule': crontab(hour=0, minute=30, day_of_month='1')
        }
    }
)
