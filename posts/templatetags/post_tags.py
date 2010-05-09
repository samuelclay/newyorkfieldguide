from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def highlight(text, word):
    return mark_safe(text.replace(word, "<span class='highlight'>%s</span>" % word))
   
@register.inclusion_tag('photoset_info.html')
def photoset_info(post, hide_subtitle=False):
    return {'post': post,
            'hide_subtitle': hide_subtitle,}
    
@register.inclusion_tag('photo_thumbs.html')
def photo_thumbs(post, per_row=4, total=12):
    photos = post.photo_set.photos.all().order_by('-order')[0:total]
    
    return {
        'post': post,
        'photos': photos,
        'per_row': per_row,
    }