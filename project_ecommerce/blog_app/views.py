from django.shortcuts import render
from blog_app.models import Blog_Post
# Create your views here.
def blog(request):
    blog_post = Blog_Post.objects.all()
    context = {"blog_post":blog_post}
    return render(request, 'blog.html', context)