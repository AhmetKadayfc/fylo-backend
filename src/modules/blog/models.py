from django.db import models
from account.models import User


class Blog_Category(models.Model):
    '''
    Model of Blog Category
    '''
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    icon_name = models.CharField(max_length=64)

    create_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    '''
    Model of Tag
    '''
    title = models.CharField(max_length=32)
    slug = models.CharField(max_length=50)

    create_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class Blog(models.Model):
    '''
    Model of Blog
    '''
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=300)
    desc = models.CharField(max_length=1000)
    cover_image = models.ImageField(upload_to='uploads/blog', null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(
        Blog_Category, on_delete=models.CASCADE, related_name='blogs')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blogs')
    tags = models.ManyToManyField(Tag)
