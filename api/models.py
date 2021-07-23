from django.db import models

class Task(models.Model):
    owner = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    due_date = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField(blank=True, default=False)

    class Meta:
        ordering = ['created']

    