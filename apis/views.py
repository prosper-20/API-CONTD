from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from .serializers import NewsSerializer
from blog.models import News

@api_view(["GET"])         # FUNCTION-BASED
def api_list_page(request):
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class Api_list_page(APIView):   # CLASS BASED
    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)



@api_view(["GET"])
def api_detail_page(request, slug): 
    if request.method == "GET":
        news = News.objects.get(slug=slug)
        serializer = NewsSerializer(news)
        return Response(serializer.data)

class Api_detail_view(APIView):
    def get(self, request, slug):
        news = News.objects.get(slug=slug)
        serializer = NewsSerializer(news)
        return Response(serializer.data)


@api_view(["POST"])
def api_create_page(request):
    serializer = NewsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Api_create_page(APIView):
    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def api_update_page(request, slug):
    try:
        news = News.objects.get(slug=slug)
    except News.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = NewsSerializer(news, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)










@api_view(['GET'])
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def post_detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
def post_update(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Post update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["DELETE"])
def post_delete(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation = post.delete()
        data = {}
        if operation:
            data["Success"] = "Post has been deleted successfully!"
        else:
            data["Failure"] = "Post deletion failed"
        return Response(data=data)


@api_view(["POST"])
def post_create(request):
    if request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):
    def get_post(self, slug):
        try:
            return Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    
    
    def get(self, request, slug):
        post = self.get_post(slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, slug):
        post = self.get_post(slug)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
        








