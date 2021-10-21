from rest_framework.response import Response
from rest_framework import generics 
from . models import Player, Post, Reply, GameData, User
from .serializers import PlayerSerializer, PostSerializer, ReplySerializer, GameDataSerializer, UserSerializer
from rest_framework.permissions import AllowAny


class PlayerList(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        username = self.request.query_params.get('username')
        queryset = queryset.filter(username = username)
        print(queryset)
        return queryset

class PlayerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = PlayerSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ReplyList(generics.ListCreateAPIView):
    # queryset = Reply.objects.all()
    serializer_class = ReplySerializer

    def get_queryset(self):
        queryset = Reply.objects.all()
        post_number = self.request.query_params.get('post_id')
        queryset = queryset.filter(post_id = post_number)
        return queryset

class ReplyAdd(generics.ListCreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

class ReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer


class GameDataList(generics.ListCreateAPIView):
    queryset = GameData.objects.all()
    serializer_class = GameDataSerializer

class GameDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GameData.objects.all()
    serializer_class = GameDataSerializer

class Register(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer