from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    """Model representing a blog."""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class BlogPost(models.Model):
    """Model representing a post within a blog."""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a simple string representing the entry."""
        if len(self.text) < 50:
            return self.text
        else:
            return f"{self.text[:50]}..."
