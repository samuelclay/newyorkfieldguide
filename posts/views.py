from django.shortcuts import get_object_or_404
from django.conf import settings
from posts.common import respond
from posts.models import Post
from syncr.flickr.models import PhotoSet


def index(request):
    posts = Post.public.all()
    
    return respond(request, 'index.html', {
        'posts': posts,
    })
    
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    return respond(request, 'post-detail.html', {
        'post': post,
    })