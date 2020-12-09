from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts") 
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, related_name="posts", blank=True, null=True) # можно было сослаться на сообщество (на модель Group)
    # укказывать сообщество при публикации необязательно, поэтому в параметрах свойства group укажите blank=True, null=True
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Group(models.Model):
    title = models.CharField(max_length = 200) # Имя 
    slug = models.SlugField(unique=True, max_length = 50) # Уникальный адрес группы, часть URL
           # (например, для группы любителей котиков slug будет равен cats: group/cats)
    description = models.TextField() # Текст, который появится на странице сообщества.
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
    


    def __str__(self):    
        return self.title
