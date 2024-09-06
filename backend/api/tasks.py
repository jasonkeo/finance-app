# myapp/tasks.py

from celery import shared_task

@shared_task
def my_periodic_task():
    # Task code here
    print("Periodic task executed!")
