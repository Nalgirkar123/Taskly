from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = [
    ('incomplete', 'Incomplete ❌'),
    ('ongoing', 'Ongoing 🔄'),
    ('complete', 'Completed ✅'),
]

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField(null=True, blank=True)
    priority_choices = [('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')]
    priority = models.CharField(max_length=6, choices=priority_choices, default='Medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='incomplete')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
