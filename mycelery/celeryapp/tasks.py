from celery.decorators import task
from celery import shared_task
from celery.utils.log import get_task_logger
from time import sleep
logger = get_task_logger(__name__)
@task(name='my_task')
def my_task(duration):
	sleep(duration)
	return('first_task_done')


# Periodic Tasks


# We can have either registered task 
@task(name='summary') 
def send_import_summary():
	print("summary.....")


@shared_task
def send_notification():
	print("Here I'm....Notification sent")