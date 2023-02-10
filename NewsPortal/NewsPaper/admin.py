from django.contrib import admin

# импортируем наши модели
from .models import Post, Category

# и зарегистрируем их
admin.site.register(Post)
#admin.site.register(Category)
