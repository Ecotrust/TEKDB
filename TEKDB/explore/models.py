from django.db import models
from ckeditor.fields import RichTextField

PAGE_CONTENT_CHOICES = (
    ('Welcome', 'Welcome'),
    ('About', 'About'),
    ('Help', 'Help'),
)

class PageContent(models.Model):
    page = models.CharField(max_length=255, choices=PAGE_CONTENT_CHOICES, primary_key=True)
    is_html = models.BooleanField(default=False)
    content = RichTextField(blank=True, null=True) #CKEditor Rich Text Editor Field
    html_content = models.TextField(blank=True, null=True, help_text='raw html if html == True')
