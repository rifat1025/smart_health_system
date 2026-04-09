from django.contrib import admin
from .models import Profile, SegmentationResult, DiseasePrediction, ChatHistory

admin.site.register(Profile)
admin.site.register(SegmentationResult)
admin.site.register(DiseasePrediction)
admin.site.register(ChatHistory)