from django.db import models
from django.core import validators


class Ticket(models.Model):
    customer_name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField()
    urgency = models.IntegerField(validators=[validators.MinValueValidator(1), validators.MaxValueValidator(5)])
    category = models.CharField(max_length=50)
    priority_score = models.FloatField()
    assigned_agent = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.category} ({self.priority_score:.2f})"
