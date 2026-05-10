from django.db import models 
import uuid
from django.conf import settings
from account.models import * 


class Category(models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 60) 

    def __str__(self):
        return self.name 



class Tags(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 60) 

    def __str__(self):
        return self.name 


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User , on_delete=models.CASCADE )
    title = models.CharField(max_length= 255)
    slug = models.SlugField(unique=True) 
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , )
    tags = models.ManyToManyField(Tags, related_name="posts" , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self): 
        return self.title 





