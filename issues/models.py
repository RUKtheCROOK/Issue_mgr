from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Priority(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Issue(models.Model):
    title = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, blank=True, null=True)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, blank=True, null=True)
    reporter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    assignee = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="assignee", blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('issue_detail', args=[str(self.id)])