from django.db import models
from django.contrib.gis.db.models import GeometryField

# Create your models here.
class Configuration(models.Model):
    # databaseName = models.CharField(max_length=255, blank=True, null=True, verbose_name='Name for DB Application')
    preferredInitialism = models.CharField(
        max_length=15, 
        default='ITK', 
        verbose_name="Preferred sharthand for traditional knowledge",
        help_text="Suggestions: 'ITK', 'TEK', etc..."
    )
    objects = models.Manager()
    # TODO: 
    #   * How to set default zoom/focus?
    #   * How to zoom to existing polygon? [This happens by default!]
    #   * How to limit drawing options to polygon only?
    #   * How to initialize drawing interaction to be 'polygon'?
    geometry = GeometryField(
        srid=3857,
        null=True, blank=True,
        verbose_name="Area of Interest",
        default=None,
        help_text="Indicate the region in which most of your 'place' records are likely exist. This serves to set the map conveniently for staff entering records. Records are allowed to exist outside of the area you indicate, and this can be changed at any time."
    )
    homepageImage = models.ImageField(
        blank=True, 
        default=None, 
        verbose_name="Homepage Image",
        help_text="If you have a preferred image for the landing page, put it here. If blank, users will see a default image."
    )
    # TODO: Allow users to:
    #   * Set hompage background color (left and right panels?)
    #   * Set homepage font-color
    #   * Override default theme colors (x8)
    # Look into Django-Colorfield: https://stackoverflow.com/a/57080102/706797 
    # Offer a 'page preview' of the homepage.

    def __unicode__(self):
        return unicode("Site Configuration: '{}' ({})".format(self.preferredInitialism, self.pk))

    def __str__(self):
        return "Site Configuration: '{}' ({})".format(self.preferredInitialism, self.pk)