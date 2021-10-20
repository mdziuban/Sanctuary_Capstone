from rest_framework.response import Response
from rest_framework import generics 
from . models import Player, Post, Reply, GameData, User
from .serializers import PlayerSerializer, PostSerializer, ReplySerializer, GameDataSerializer
from rest_framework.permissions import IsAuthenticated


class PlayerList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = PlayerSerializer

class PlayerDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = PlayerSerializer

class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ReplyList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ReplySerializer

    def get_queryset(self):
        queryset = Reply.objects.all()
        post_number = self.request.query_params.get('post_id')
        queryset = queryset.filter(post_id = post_number)
        return queryset

class ReplyAdd(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

class ReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer


class GameDataList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = GameData.objects.all()
    serializer_class = GameDataSerializer

class GameDataDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = GameData.objects.all()
    serializer_class = GameDataSerializer
