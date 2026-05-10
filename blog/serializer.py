from rest_framework import serializers
from .models import Post , Category , Tags

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'title',
            'slug',
            'content',
            'excerpt',
            'category',
            'tags',
            'created_at',
        ]
        read_only_fields = ['id', 'author', 'created_at']

class CategorySerializer(serializers.ModelSerializer): 
    class Meta :
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'