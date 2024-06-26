from django.db import models

class SearchResult(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.title

