import logging
from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.views import View
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import cache_page

from portal.settings import NUMBER_OF_POSTS
from blog.models import Post, PostTag, Tag
from blog.forms import SignInForm, MlPromobotInForm
from api.service import ThrottlingForecasts, forecast

logger = logging.getLogger("__name__")
throttler = ThrottlingForecasts(limit=3, interval=(60))


def paginate_queryset(object, request):
    paginator = Paginator(object, NUMBER_OF_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


# Главная страница
@cache_page(60 * 1)
def index(request):
    template = 'posts/index.html'
    user = request.user
    post = Post.objects.filter(posting=True).prefetch_related(
        'tags'
    ).select_related('author',).order_by('-pub_date')
    page_obj = paginate_queryset(post, request)
    context = {
        'title': 'Последние обновления',
        'page_obj': page_obj,
        'user': user
    }
    return render(request, template, context)


def post_detail(request, post_slug):
    post = get_object_or_404(Post, url=post_slug)
    template = 'posts/post_detail.html'
    user = request.user
    tags = post.tags.all()
    context = {
        'post': post,
        'title': post.title,
        'tags': tags,
        'user': user
    }
    return render(request, template, context)


@method_decorator(csrf_protect, name='post')
class SignInView(View):
    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(request, 'registration/signin.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'registration/signin.html', context={
            'form': form,
        })


@method_decorator(csrf_protect, name='post')
class MlPromobotInView(View):
    template = 'prototype/ml_promobot.html'

    def get(self, request, *args, **kwargs):
        form = MlPromobotInForm()
        return render(request, self.template, context={'form': form,})

    def post(self, request, *args, **kwargs):
        form = MlPromobotInForm(request.POST)
        if form.is_valid():
            if throttler():
                logger.info("go forecast")
                result = forecast(form.cleaned_data['text'])
            else:
                logger.warning("Превышен лимит запросов к forecast")
                result = {'error':'Превышен лимит запросов. Пожалуйста, попробуйте позже.'}
        return JsonResponse({'form': str(form), 'result': result})
