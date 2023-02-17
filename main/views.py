from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Category, Post, PostImage
from .serializers import CategorySerializer, PostSerializer, PostImageSerializer
from rest_framework.response import Response
# from rest_framework.views import APIView # для вьюшек apiviews
from rest_framework import generics

# @api_view(['GET'])
# def categories(request):
#     categories = Category.objects.all() # создаем переменную катигорис, в которой будет храниться все обьекты из модельки категорис.Обьект это менеджер
#     serializer = CategorySerializer(categories, many=True)# обязательно определять переменную сериалайзер для того чтобы передовать джейсон формат наших обьектов, которых мы сериализовали в модельке categoryserializer
#     return Response(serializer.data)
    

# class PostListView(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         post = request.data 
#         serializer = PostSerializer(data=post)
#         if serializer.is_valid(raise_exception=True):
#             post_saved = serializer.save()
            
#         return Response(serializer.data) 

# genericViews он легче, и упрощает код разработчика
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostView(generics.ListCreateAPIView): # мы сделали одним запросом get&post для нашего поста
    queryset = Post.objects.all()  
    serializer_class = PostSerializer  

class PostDetailView(generics.RetrieveAPIView):# если мы хотим получить об одном посте
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()  
    serializer_class = PostSerializer

class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer    

class PostImageView(generics.ListAPIView):
    queryset = PostImage.objects.all()   
    serializer_class = PostImageSerializer 

    def get_serializer_context(self):
        return {'request': self.request}



# class PostCreateView(generics.CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
