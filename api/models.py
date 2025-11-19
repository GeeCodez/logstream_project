from django.db import models

# Create your models here.
class logEntry(models.Model):
    LEVEL_CHOICES=[
        ('DEBUG','Debug'),
        ('INFO', 'Info'),
        ('WARNING', 'Warning'),
        ('ERROR','Error'),
        ('CRITICAL', 'Critical'),
    ]
    service_name=models.CharField(max_length=100, db_index=True)
    timestamp=models.DateTimeField(auto_now_add=True, db_index=True)
    level=models.CharField(max_length=10,choices=LEVEL_CHOICES, db_index=True)
    message=models.TextField()

    class Meta:
        ordering=['-timestamp']

    def __str__(self):
        return f"[{self.service_name} {self.timestamp}-{self.level}: {self.message}]"