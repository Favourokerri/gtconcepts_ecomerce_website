from django.shortcuts import render, get_object_or_404
from blog_app.models import Blog_Post
from blog_app.emails import send_mail_after_blog_post
# Create your views here.


def blog(request):
    """ view for blog """
    blog_post = Blog_Post.objects.all()
    context = {"blog_post": blog_post}
    return render(request, 'blog.html', context)

def blog_post_detail(request, primary_key):
     post = get_object_or_404(Blog_Post, id=int(primary_key))
     blog_post = Blog_Post.objects.all()
     context = {"blog_post": blog_post,
                "post": post
                }
     return render(request, 'blog_post_detail.html', context)
