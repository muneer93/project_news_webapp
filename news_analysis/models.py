from django.db import models

class VideoAnalysis(models.Model):
    video_title = models.CharField(max_length=200)
    channel_name = models.CharField(max_length=200)
    bias_score = models.FloatField()
    sentiment = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.video_title
