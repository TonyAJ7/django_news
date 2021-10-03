from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView

from .forms import CommentForm
from .models import *


def home(request):
    news = News.objects.all().order_by('-created')
    global_new = News.objects.last()
    latest = News.objects.all().order_by('-created')[1:4]
    paginator = Paginator(news, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    category = Category.objects.all().order_by('name')
    context = {
        'news': news,
        'global_new': global_new,
        'latest': latest,
        'page_obj': page_obj,
        'category': category,
    }
    return render(request, 'home.html', context)


class NewDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'
    form = CommentForm

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return redirect(reverse('news-detail', kwargs={'pk': post.pk}))

    def get_context_data(self, **kwargs):
        post_comments = Comment.objects.all().filter(post=self.object.id)
        post_comments_count = Comment.objects.all().filter(post=self.object.id).count()
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        context['post_comments'] = post_comments
        context['post_comments_count'] = post_comments_count
        return context


def about(request):
    return render(request, 'aboutus.html')


def feedback(request):
    return render(request, 'contactus.html')

