from django.contrib import admin
from .models import Player, Post, Reply, GameData

admin.site.register(Player)
admin.site.register(Post)
admin.site.register(Reply)
admin.site.register(GameData)