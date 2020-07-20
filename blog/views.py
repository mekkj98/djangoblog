from django.shortcuts import render
from django.views import generic
from .models import Post

# about the website
def About(request):
    return render(request,'about.html')


# show list of blog posts
class PostList(generic.ListView):
    paginate_by = 6
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


# show single blog posts 
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog.html'