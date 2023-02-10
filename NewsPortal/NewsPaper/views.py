from django.shortcuts import render

# импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView

# импортируем модель Product из models.py
from .models import Post
from pprint import pprint

# создадим модель объектов, которые будем выводить
class PostsList(ListView):
    # название модели из файла models.py
    model = Post  # в нашем случае модель - Post (статья/новость)
    ordering = 'date_created'

    # ссылка на шаблон странички, в данном случае файл templates/news.html
    template_name = 'news.html'

    context_object_name = 'news'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next_post'] = None
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'

    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next_post'] = None
        pprint(context)
        return context