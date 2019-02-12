from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from markdown import markdown


class Post(models.Model):  # Inherits from database model (creates entries in a DB when the fields are filled)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def content_as_markdown(self):
        return mark_safe(markdown(self.content, safe_mode='escape'))  # TODO Put some HTML XSS filtering in (security)

    def __str__(self):
        return self.title
