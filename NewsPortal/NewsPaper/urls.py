# импортируем библиотеку для работы с путями urls
from django.urls import path
# импортируем наше представление
from .views import PostsList, PostDetail, SearchList, NewsCreate, NewsUpdate, NewsDelete, PostCreate

urlpatterns = [
    # путь ко всем товарам (пустой)
    path('news/', PostsList.as_view(),name='post_list'),
    path('<int:pk>', PostDetail.as_view(),name='post_detail'),
    path('search/', SearchList.as_view(),name='news_search'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('post/create/', PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', NewsUpdate.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', NewsDelete.as_view(), name='post_delete'),
]