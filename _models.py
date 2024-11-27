# _models.py

from django.db import models

# Create your models here.

class Article(models.Model):
    id_article = models.IntegerField()
    autor = models.CharField(max_lenght=100)
    title = models.CharField(max_lenght=100)
    teg = models.CharField(max_lenght=20)
    text = models.TextField(max_lenght=1000)
    create_dt = models.DateTimeField(auto_now_add=True)

class ListBooks(models.Model):
   id_book = models.IntegerField()
   autor = models.CharField(max_lenght=100)
   year = models.IntegerField()
   literary_genre = models.CharField(max_lenght=100)
   biography = models.CharField(max_lenght=1000)


class User(models.Model):
    id_user = models.IntegerField()
    first_name = models.CharField(max_lenght=100)
    last_name = models.CharField(max_lenght=100)
    birthday_dt = ''


class UserBooks(models.Model):
    id_book = models.IntegerField()
    done = models.CharField(max_lenght=100)
    in_process = models.CharField(max_lenght=100)
    planned = models.CharField(max_lenght=100)
    favorite = models.CharField(max_lenght=100)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    autor = models.CharField(max_lenght=100)
    text = models.TextField(max_lenght=1000)
    create_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        index = self.text.find(' ', 30)
        text = self.text[:index]
        return f'{self.autor}: {text}...'

