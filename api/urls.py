from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LogEntryViewsets

router=DefaultRouter()
router.register(r"logs", LogEntryViewsets, basename="logentry")

urlpatterns=[
    path('',include(router.urls))
]