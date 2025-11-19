from rest_framework import serializers
from .models import logEntry

class logEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model=logEntry
        fields="__all__"

        read_only_fields=['timestamp']