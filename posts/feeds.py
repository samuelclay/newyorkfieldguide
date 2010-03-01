from django.contrib.syndication.feeds import Feed
from posts.models import Post
from django.core.urlresolvers import reverse

class LatestEntriesFeed(Feed):
    title = "New York Field Guide"
    link = '/'
    description = "The Historic Districts of New York City."

    item_author_name = "Samuel Clay"
    item_author_link = "http://www.samuelclay.com"
        
    def items(self):
        return [{'photos': obj.photo_set.photos.all().order_by('order'), 'post': obj} for obj in Post.public.order_by('-publish_date')[:20]]

    def item_link(self, item):
        return item['post'].get_absolute_url()
        
    def item_title(self, item):
        return item['post'].title

    def item_description(self, item):
        return item['post'].subtitle
        
    def item_pubdate(self,item):
        return item['post'].publish_date