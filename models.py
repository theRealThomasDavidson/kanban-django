from django.db import models
from django import forms

int_to_status = {
    0: "create",
    1: "backlog",
    2: "design",
    3: "write",
    4: "review",
    5: "testing",
    6: "done",
    7: "hidden",
    8: "In Progress",
}


# Create your models here.


class Task(models.Model):

    Choices = []
    for ii in int_to_status:
        Choices.append((ii, int_to_status[ii].upper()))
    title = models.CharField(max_length=250, null=False, blank=False)
    status = models.IntegerField(choices=Choices, default=1)
    def __str__(self):
        return "{} :{}".format(self.title, int_to_status[self.status])


    def save(self, *args, **kwargs):
        a = self.taskupdate_set.order_by("-time")
        if a:
            if self.status not in int_to_status:
                raise ValueError("status not in appropiate range of {}".format(int_to_status))
                return
            if self.status == a[0].new_status:
                super(Task, self).save(*args, **kwargs)
                return

            b = TaskUpdate(old_status=a[0].new_status, new_status=self.status, task= self)
        else:
            b = TaskUpdate(old_status=0, new_status=self.status, task=self)
        super(Task, self).save(*args, **kwargs)
        b.save()
        return


class TaskUpdate(models.Model):
    class Meta:
        ordering = ['-time']
    Choices = []
    for ii in int_to_status:
        Choices.append((ii, int_to_status[ii].upper()))
    old_status = models.IntegerField(choices=Choices)
    new_status = models.IntegerField(choices=Choices)
    time = models.DateTimeField(auto_now=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return "{} -> {}".format(self.task.title, int_to_status[self.old_status], int_to_status[self.new_status])


class TaskNote(models.Model):
    class Meta:
        ordering = ['-time']
    Choices = []
    for ii in int_to_status:
        Choices.append((ii, int_to_status[ii].upper()))
    status = models.IntegerField(choices=Choices)
    time = models.DateTimeField(auto_now=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    note = models.TextField(blank=False)

    def __str__(self):
        return "{} ({}|{}): {}".format(self.task.title, int_to_status[self.status], self.time, self.note)
