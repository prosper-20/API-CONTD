from rest_framework import generics
from .models import Post
from .serializers import PostSerializer, UserRegistrationSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



@api_view(["POST"])
def api_register_view(request):
    if request.method == "POST":
        serilaizer = UserRegistrationSerializer(data=request.data)
        data = {}
        if serilaizer.is_valid():
            user = serilaizer.save()
            data["Success"] = "Account creation successful"
            data["username"] = user.username
            data["email"] = user.email
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)

