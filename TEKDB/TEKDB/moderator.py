from moderation import moderation
from moderation.db import ModeratedModel
from moderation.moderator import GenericModerator

from .models import *

# class AnotherModelModerator(ModelModerator):
# class PlacesModelModerator(ModeratedModel):
class PlacesModelModerator(GenericModerator):
    # Add your moderator settings for AnotherModel here
    a='foo'
#
#
# moderation.register(YourModel)  # Uses default moderation settings
# moderation.register(Places)  # Uses default moderation settings
# moderation.register(Places, ModeratedModel)  # Uses default moderation settings
moderation.register(Places)  # Uses default moderation settings
moderation.register(Resources)  # Uses default moderation settings
moderation.register(ResourcesActivityEvents)  # Uses default moderation settings
moderation.register(Citations)  # Uses default moderation settings
moderation.register(Media)  # Uses default moderation settings
moderation.register(PlaceAltIndigenousName)  # Uses default moderation settings
moderation.register(PlaceGISSelections)  # Uses default moderation settings
moderation.register(PlacesCitationEvents)  # Uses default moderation settings
moderation.register(PlacesMediaEvents)  # Uses default moderation settings
# moderation.register(AnotherModel, AnotherModelModerator)  # Uses custom moderation settings
