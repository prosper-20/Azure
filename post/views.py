from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from .models import Post
from .serializers import Postserializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication



@api_view(["GET"])
def api_post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = Postserializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def api_post_detail(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = Postserializer(post)
        return Response(serializer.data)



class Api_post_list(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializer
    authentication_classes = (TokenAuthentication,)



class Api_post_detail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializer
