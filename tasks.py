from celery_worker import celery
from docker_utils import get_unhealthy_containers, restart_container

@celery.task
def restart_unhealthy_containers():
    unhealthy = get_unhealthy_containers()
    for c in unhealthy:
        restart_container(c)
