from django.db import models
from django.contrib.gis.db.models import GeometryField
from tinymce.models import HTMLField
from colorfield.fields import ColorField
from django.conf import settings


# Create your models here.
class Configuration(models.Model):
    preferredInitialism = models.CharField(
        max_length=15,
        default="ITK",
        blank=True,
        verbose_name="Preferred sharthand for traditional knowledge",
        help_text="Suggestions: 'ITK', 'TEK', etc...",
    )

    preferredInitialismPlacementChoices = [
        ("default", "Align Center"),
        ("before", "Align Left"),
        ("after", "Align Right"),
    ]

    preferredInitialismPlacement = models.CharField(
        default=preferredInitialismPlacementChoices[0],
        choices=preferredInitialismPlacementChoices,
        max_length=255,
        help_text="Select the position of the preferred initialism in relative to the logo.",
    )

    LOGO_CHOICES = [
        ("/static/explore/img/logos/logo_weave.svg", "Weave"),
        ("/static/explore/img/logos/logo_drop.svg", "Droplet"),
        ("Other", "Custom"),
    ]

    logo_help_text = (
        "Choose your logo for the site header. You can choose between: <ul>"
    )
    for logo_choice in LOGO_CHOICES[:-1]:
        logo_help_text += '<li style="padding-left: 1rem">\'{}\' <img src="{}" style="max-width: 70px; padding:0.5rem; background-color:white"></li>'.format(
            logo_choice[1], logo_choice[0]
        )
    logo_help_text += "<li>Or choose 'Custom' and add your own using the <b>Header Logo Override Image</b> field.</li></ul>"

    logo = models.CharField(
        default=LOGO_CHOICES[0],
        choices=LOGO_CHOICES,
        max_length=255,
        help_text=logo_help_text,
    )

    logo_override = models.ImageField(
        blank=True,
        null=True,
        default=None,
        verbose_name="Header Logo Override Image",
        help_text="Use this to add your own logo to the site header",
    )

    objects = models.Manager()
    # TODO:
    #   * How to limit drawing options to polygon only?
    #   * How to initialize drawing interaction to be 'polygon'?
    geometry = GeometryField(
        srid=3857,
        null=True,
        blank=True,
        verbose_name="Area of Interest",
        default=None,
        help_text="Indicate the region in which most of your 'place' records are likely to exist. This serves to set the map conveniently for staff entering records. Records are allowed to exist outside of the area you indicate, and this can be changed at any time.",
    )
    homepage_image = models.ImageField(
        blank=True,
        default=None,
        verbose_name="Homepage Image",
        help_text="If you have a preferred image for the landing page, put it here. If blank, users will see a default image.",
    )
    homepage_image_attribution = HTMLField(
        blank=True,
        null=True,
        default=None,
        verbose_name="Homepage Image attribution",
        help_text="If using a custom image that requires attribution for use, please provide that here.",
    )  # TinyMCE HTML Field

    COLOR_PALETTE = []

    for key in settings.PROJ_CSS.keys():
        COLOR_PALETTE.append((settings.PROJ_CSS[key], key))

    COLOR_PALETTE.append(("#FFFFFF", "white"))
    COLOR_PALETTE.append(("#000000", "black"))

    homepage_font_color = ColorField(
        default="#FFFFFF",
        help_text="Text color on homepage. Recommended: White (#FFFFFF).",
        verbose_name="Homepage Text Color",
        samples=COLOR_PALETTE,
    )

    homepage_left_background = ColorField(
        default="#000000",
        help_text="Background color behind Text on homepage. Recommended: Black (#000000).",
        verbose_name="Left Homepage Background Color",
        samples=COLOR_PALETTE,
    )

    homepage_right_background = ColorField(
        default="#000000",
        help_text="Background color behind image on homepage. Recommended: Black (#000000).",
        verbose_name="Right Homepage Background Color",
        samples=COLOR_PALETTE,
    )

    max_results_returned = models.IntegerField(
        default=500,
        verbose_name="Maximum no. of search results",
        help_text="500 is recommended. Allowing more may result in poor website performance or strain on the server.",
    )

    #   * Making search settings customizable by admin

    SEARCH_RANK_CHOICES = [
        (0.01, "Lowest"),
        (0.1, "Default"),
        (0.6, "Moderate"),
        (0.9, "Highest"),
    ]

    min_search_rank = models.FloatField(
        default=None,
        choices=SEARCH_RANK_CHOICES,
        max_length=255,
        verbose_name="Minimum Search Rank",
        help_text="The lowest acceptable ranking score assigned to search results.",
        null=True,
        blank=True,
    )

    SEARCH_SIMILARITY_CHOICES = [
        (0.01, "Permissive"),
        (0.1, "Default"),
        (0.3, "Similar"),
        (0.4, "Has Match"),
        (0.9, "Exact Match"),
    ]

    min_search_similarity = models.FloatField(
        default=None,
        choices=SEARCH_SIMILARITY_CHOICES,
        max_length=255,
        verbose_name="Minimum Search Similarity",
        help_text="The lowest threshold for similar search results to be included in results.",
        null=True,
        blank=True,
    )

    # TODO: Allow users to:
    #   * Override default theme colors (x8)
    # Look into Django-Colorfield: https://stackoverflow.com/a/57080102/706797
    # Offer a 'page preview' of the homepage.

    # place_icon': 'explore/img/icons/i_place.svg',
    # place_icon_override
    # place_name_override
    # resource_icon': 'explore/img/icons/i_resource.svg',
    # resource_icon_override
    # resource_name_override
    # activity_icon': 'explore/img/icons/i_activity.svg',
    # activity_icon_override
    # activity_name_override
    # source_icon': 'explore/img/icons/i_source.svg',
    # source_icon_override
    # source_name_override
    # media_icon': 'explore/img/icons/i_media.svg',
    # media_icon_override
    # media_name_override

    def __unicode__(self):
        return unicode(
            "Site Configuration: '{}' ({})".format(self.preferredInitialism, self.pk)
        )

    def __str__(self):
        return "Site Configuration: '{}' ({})".format(self.preferredInitialism, self.pk)
