from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(null=False, blank=False)
    finish_at = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")

    class Meta:
        ordering = ["-deadline"]

    def mark_has_complete(self):
        if not self.finish_at:
            self.finish_at = date.today()
            self.save()
