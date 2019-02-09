from django.shortcuts import render
from blog.models import Comment,Post
from django.utils import timezone
from django.views.generic import TemplateView,ListView,DetailView

# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')

class PostDetailView(DetailView):
    model = Post
