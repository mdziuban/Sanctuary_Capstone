from rest_framework import serializers
from .models import Player, Post, Reply, GameData, User

class PlayerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = User
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Post
        fields = '__all__'

class ReplySerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Reply
        fields = '__all__'
    
class GameDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameData
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user

    def update(self, *args, **kwargs):
        user = super().update(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user

    class Meta:
        model = User
        fields = "__all__" 
