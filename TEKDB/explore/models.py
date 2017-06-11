from django.db import models
from ckeditor.fields import RichTextField

PAGE_CONTENT_CHOICES = (
    ('Welcome', 'Welcome'),
    ('About', 'About'),
    ('Help', 'Help'),
)

class PageContent(models.Model):
    page = models.CharField(max_length=255, choices=PAGE_CONTENT_CHOICES, primary_key=True)
    content = RichTextField(blank=True, null=True, config_name="custom") #CKEditor Rich Text Editor Field
    is_html = models.BooleanField(default=False, help_text='Select this if you want to use raw HTML instead. For this option, use the "HTML content" window below.')
    html_content = models.TextField(blank=True, null=True, help_text='raw html if html == True')

    class Meta:
        verbose_name_plural = 'Page Contents'

    def __unicode__(self):
        return unicode("%s" % (self.page))

    def __str__(self):
        return self.page
