from celery.schedules import crontab


from celery import Celery

celery = Celery(
    "worker",
    broker="redis://redis:6379/0",
    include=["tasks"]
)

celery.conf.beat_schedule = {
    "restart-unhealthy-every-1-minute": {
        "task": "tasks.restart_unhealthy_containers",
        "schedule": crontab(minute="*/1"),  # every 1 minute
    }
}
