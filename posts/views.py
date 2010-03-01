from django.shortcuts import get_object_or_404
from django.conf import settings
from posts.common import respond
from posts.models import Post, Callout
from syncr.flickr.models import PhotoSet


def index(request):
    posts = Post.public.all()
    
    return respond(request, 'index.html', {
        'posts': posts,
    })
    
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    photos = post.photo_set.photos.all().order_by('order')
    callouts = Callout.objects.filter(post=post)
    footer_post_borough = get_random_post(post, 'borough')
    footer_post_elsewhere = get_random_post(post, 'elsewhere')
    
    return respond(request, 'post-detail.html', {
        'post': post,
        'photos': photos,
        'callouts': callouts,
        'footer_post_borough': footer_post_borough,
        'footer_post_elsewhere': footer_post_elsewhere,
    })
    
def photo_detail(request, slug, **kwargs):
    pass
    
def get_random_post(post, location):
    index = 0
    if location == 'borough':
        posts = Post.public.filter(borough=post.borough).order_by('?')
    elif location == 'elsewhere':
        posts = Post.public.exclude(borough=post.borough).order_by('?')

    if posts:
        for i, p in enumerate(posts):
            if p != post:
                index = i
                break
            
        if posts[index]:
            return posts[index]