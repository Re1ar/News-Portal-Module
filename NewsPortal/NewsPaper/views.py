from datetime import datetime

from django.http import request, HttpRequest
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .Forms import PostForm
from django.shortcuts import render

# импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# импортируем модель Product из models.py
from .models import Post
from pprint import pprint
from .filters import PostFilter
# создадим модель объектов, которые будем выводить
class PostsList(ListView):
    # название модели из файла models.py
    model = Post  # в нашем случае модель - Post (статья/новость)
    ordering = 'date_created'

    # ссылка на шаблон странички, в данном случае файл templates/news.html
    template_name = 'news.html'
    paginate_by = 10
    context_object_name = 'news'


    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next_post'] = None
        context['filterset'] = self.filterset
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

class SearchList(ListView):
    model = Post

    template_name = 'search.html'
    paginate_by = 10
    context_object_name = 'news'

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next_post'] = None
        context['filterset'] = self.filterset
        return context

class NewsUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'news_update.html'

class NewsDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    template_name = 'post_delete.html'


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    #@login_required
    def form_valid(self, form):
        post = form.save(commit=False)
        #form.instance.author = HttpReq
        post.post_author_id = 1
        post.category = 'A'
        return super().form_valid(form)

class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'
    def form_valid(self, form):
        post = form.save(commit=False)
        #form.instance.author = HttpReq
        post.post_author_id = 1
        post.category = 'N'
        return super().form_valid(form)