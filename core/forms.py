from django import forms
from .models import SegmentationResult

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = SegmentationResult
        fields = ['original_image']