from django.db import models
from datetime import time, datetime
from django.conf import settings
# Create your models here.

class BaseTask(models.Model):

    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('IN_PROGRESS','In_progress'),
        ('DONE','Done')
    )
    # Abstract for all task model
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES, 
                              default=STATUS_CHOICES[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class  Meta:
        abstract =  True
        ordering = ['-created_at', '-updated_at']

class WeekDay(models.Model):
    DAYS_CHOICES = (
        ('MON', 'Mon'),
        ('TUE', 'Tue'),
        ('WED', 'Wed'),
        ('THU', 'Thu'),
        ('FRI', 'Fri'),
        ('SAT', 'Sat'),
        ('SUN', 'Sun'),
    )
    value = models.CharField(choices=DAYS_CHOICES, 
                             max_length=10, unique=True)
    

class TaskReminder(models.Model):
    time = models.TimeField(default=time(0,0,0,0))
    weekday = models.ForeignKey(WeekDay, on_delete=models.CASCADE,
                             null=False, related_name='reminders')
    
    class Meta:
        ordering = ['-weekday', '-time']
        unique_together = ['time', 'weekday']

class TodoTask(BaseTask):
    reminder = models.ManyToManyField(TaskReminder, 
                                      related_name='tasks', 
                                      blank=True)
    subtasks = models.ForeignKey('self', on_delete=models.CASCADE, 
                                 null=True, blank=True, 
                                 related_name='parent_task')
    deadline = models.DateTimeField(null=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
                              