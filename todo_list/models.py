from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=63)

    def __str__(self):
        return self.title


class Task(models.Model):
    content = models.TextField()
    was_created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, default=None)
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['status', 'was_created']

    def __str__(self):
        return self.content
