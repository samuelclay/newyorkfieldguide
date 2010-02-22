import datetime
from django.db import models


class PublicPostManager(models.Manager):
    """
    Standard .objects manager, just with a public filter.
    """
    def get_query_set(self):
        return super(PublicPostManager, self).get_query_set().filter(
            is_public=True,
            publish_date__lte=datetime.datetime.now()
        )