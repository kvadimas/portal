from django.shortcuts import render
from django.core.paginator import Paginator

from portal.settings import NUMBER_OF_POSTS
from blog.models import Post

def paginate_queryset(object, request):
    paginator = Paginator(object, NUMBER_OF_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


# Главная страница
def index(request):
    template = 'posts/index.html'
    post = Post.objects.prefetch_related('tags').select_related(
        'author',
    ).order_by('pub_date')
    page_obj = paginate_queryset(post, request)
    context = {
        'title': 'test',
        'page_obj': page_obj,
    }
    return render(request, template, context)
