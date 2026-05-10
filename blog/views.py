from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import *
from .serializer import *

class Postapiview(APIView):
    def get(self , request):
        post = Post.objects.all().order_by('created_at')
        serializer = PostSerializer(post , many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)