from django.db import models
from posts.managers import PublicPostManager
from syncr.flickr.models import PhotoSet


class Post(models.Model):
    BROOKLYN = "brooklyn"
    BRONX = "bronx"
    STATENISLAND = "statenisland"
    QUEENS = "queens"
    MANHATTAN = "manhattan"
    BOROUGH_CHOICES = (
        (BROOKLYN, "Brooklyn"),
        (BRONX, "The Bronx"),
        (QUEENS, "Queens"),
        (STATENISLAND, "Staten Island"),
        (MANHATTAN, "Manhattan"),
    )
    
    title = models.CharField(max_length=255)
    subtitle = models.TextField(blank=True, null=True)
    slug = models.SlugField()
    photo_set = models.ForeignKey(PhotoSet)
    
    borough = models.CharField(max_length=50,
                               default=BROOKLYN,
                               choices=BOROUGH_CHOICES)
    coordinates = models.CharField(max_length=255, default="40.685935,-73.986214")
    zoom = models.IntegerField(default=15)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)
    
    public = PublicPostManager()
    objects = models.Manager()
    
    def __unicode__(self):
        return "%s: %s (%s)" % (
            self.title,
            self.photo_set.title,
            self.publish_date,
        )
    
    @models.permalink
    def get_absolute_url(self):
        return ('post-detail', (), {'slug': self.slug})



class Callout(models.Model):
    DETAIL = 'detail'
    BACKGROUND = 'background'
    QUOTE = 'quote'
    LINK = 'link'
    CALLOUT_CHOICES = (
        (DETAIL, 'Detail'),
        (BACKGROUND, 'Background'),
        (QUOTE, 'Quote'),
        (LINK, 'Link'),
    )
    
    post = models.ForeignKey(Post)
    content = models.TextField(null=True, blank=True)
    content_type = models.CharField(max_length=50,
                                    default=BACKGROUND,
                                    choices=CALLOUT_CHOICES)
    order = models.IntegerField(default=1)
    date = models.DateTimeField()
    link = models.TextField(null=True, blank=True)
    quote_speaker = models.CharField(max_length=255, null=True, blank=True)
    detail_image_url = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return "[#%s] %s" % (
            self.order,
            self.post,
        )