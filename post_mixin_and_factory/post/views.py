from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework import serializers
from rest_framework.response import Response

from post.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post

class PostParamSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()

class PostListCreateView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        param = PostParamSerializer(data=request.data)
        param.is_valid(raise_exception=True)

        post = Post(**param.validated_data)
        post.save()
        return Response(PostSerializer(post).data)


