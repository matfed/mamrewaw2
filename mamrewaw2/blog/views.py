from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from blog.models import Post, RecordingSet

def index(request):
    posts = Post.objects.order_by('date')
    return render_to_response('blog/index.html', {'posts': posts}, context_instance=RequestContext(request))

def post(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    return render_to_response('blog/post.html', {'post': p}, context_instance=RequestContext(request))

def recordings(request):
    sets = RecordingSet.objects.order_by('date')
    return render_to_response('blog/recordings.html', {'recsets': sets}, context_instance=RequestContext(request))
