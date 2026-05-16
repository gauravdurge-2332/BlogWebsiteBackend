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
    
    def post(self,request): 
        serailzer = PostSerializer(data = request.data) 

        if serailzer.is_valid() :
            serailzer.save() 

            return Response(serailzer.data) 
        
        return Response({'Error' : 'There is the error'})
            
class CategoryApiview(APIView):

    def get(self, request):

        data = Category.objects.all()

        serializer = CategorySerializer(data, many=True)

        return Response(serializer.data)
         


    def post(self , request):
            serailizer = CategorySerializer(data = request.data)
            if serailizer.is_valid() :
                serailizer.save() 

                return Response({"result" : 'Response Posted successfully'})
    
            return Response({'result' : 'Error in posting data'})
    

class TagApiView(APIView):
     
     def post(self , request):
          data = TagSerializer(data = request.data , many=True) 

          if data.is_valid() : 
               data.save() 

               return Response({'result' : 'Data posted successfully'})
          return Response({'result' : 'Error in posting the data'})
     
     def get(self , request): 
          data = Tags.objects.all() 
          serailizer = TagSerializer(data,many = True) 

          return Response(serailizer.data)
    
