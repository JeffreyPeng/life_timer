from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

class UserState(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_start = models.BooleanField(default=False)
    last_start_time = models.DateTimeField(auto_now_add=True)
    last_start_topic = models.ForeignKey(
        'Topic',
        models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.user.username + ': is_start=' + str(self.is_start)

class Topic(models.Model):
    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    total_delta = models.DurationField(default=timedelta(0))
    parent = models.ForeignKey(
        'self',
        models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.text

class Record(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    loss_delta = models.DurationField()
    delta = models.DurationField()

    def __str__(self):
        return self.topic.text + ': delta=' + str(self.delta)