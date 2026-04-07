from django.db import models
from django.contrib.auth.models import User


# 👤 USER PROFILE
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


# 🖼️ SEGMENTATION MAIN MODEL
class SegmentationResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    original_image = models.ImageField(upload_to='segmentation/original/')
    mask_image = models.ImageField(upload_to='segmentation/mask/', blank=True, null=True)
    overlay_image = models.ImageField(upload_to='segmentation/overlay/', blank=True, null=True)

    model_name = models.CharField(max_length=100, default="U-Net")
    confidence_score = models.FloatField(blank=True, null=True)

    predicted_region = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Segmentation {self.id}"


# 🧠 DISEASE PREDICTION (LINKED TO SEGMENTATION)
class DiseasePrediction(models.Model):
    segmentation = models.OneToOneField(
        SegmentationResult,
        on_delete=models.CASCADE,
        related_name="prediction"
    )

    disease_name = models.CharField(max_length=100)

    severity = models.CharField(
        max_length=20,
        choices=[
            ("low", "Low"),
            ("medium", "Medium"),
            ("high", "High"),
        ],
        default="low"
    )

    probability = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.disease_name


# 💬 CHATBOT HISTORY
class ChatHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    message = models.TextField()
    response = models.TextField()

    image = models.ImageField(upload_to='chat/images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} chat {self.id}"