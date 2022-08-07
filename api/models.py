from venv import create
from django.db import models


class WorkType(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return str(self.id)+"-"+str(self.name)

    class Meta:
        db_table = 'workType'


class Work(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(
        WorkType, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.id)+"-"+str(self.name)

    class Meta:
        db_table = 'work'


class Stock(models.Model):
    name = models.CharField(max_length=25)
    num = models.IntegerField(default=0)
    add_work = models.ForeignKey(
        Work, on_delete=models.SET_NULL, null=True, blank=True, related_name='add_work')
    decrease_work = models.ForeignKey(
        Work, on_delete=models.SET_NULL, null=True, blank=True, related_name='decrease_work')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+"-"+str(self.name)


class Reminder(models.Model):
    day = models.IntegerField()
    work = models.ForeignKey(
        Work, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.id)+"-reminder-"+str(self.work.name)


class Record(models.Model):
    work = models.ForeignKey(
        Work, on_delete=models.CASCADE, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.id) + "-record+" + str(self.created_at)
