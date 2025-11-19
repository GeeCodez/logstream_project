from django.shortcuts import render
from rest_framework import viewsets
from .serializers import logEntrySerializer
from .models import logEntry

class LogEntryViewsets(viewsets.ModelViewSet):
    queryset=logEntry.objects.all()
    serializer_class=logEntrySerializer