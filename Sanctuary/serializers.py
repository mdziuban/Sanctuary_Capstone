from rest_framework import serializers
from .models import Player, Post, Reply, GameData, SiteImages, User


class PlayerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Player
        fields = '__all__'

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """
    
    def __init__(self, *args, **kwargs):
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        fields = self.context['request'].query_params.get('fields')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


# class UserSerializer(DynamicFieldsModelSerializer, serializers.HyperlinkedModelSerializer):
#     player = PlayerSerializer(read_only=True)
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'first_name', 'last_name')


class UserSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)
    class Meta: 
        model = User
        fields = '__all__'
class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    # user = UserSerializer(read_only = True)
    class Meta:
        model = Post
        fields = '__all__'

class PostDetailSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='user.username', read_only=True)
    user = UserSerializer(read_only = True)
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


class RegisterSerializer(serializers.ModelSerializer):
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
        

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteImages
        fields = "__all__"
