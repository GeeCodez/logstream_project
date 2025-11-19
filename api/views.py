from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .serializers import logEntrySerializer
from .models import logEntry

class LargeResultPagination(PageNumberPagination):
    page_size=100
    page_size_query_params='page_size'
    max_page_size=10000

class LogEntryViewsets(viewsets.ModelViewSet):
    queryset=logEntry.objects.all()
    serializer_class=logEntrySerializer
    pagination_class=LargeResultPagination