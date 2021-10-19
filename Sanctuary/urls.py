from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from . views import PlayerList, PlayerDetails, PostList, PostDetail, ReplyList, ReplyAdd, ReplyDetail, GameDataList, GameDataDetail

urlpatterns = [
    path('player/', PlayerList.as_view(), name='player_list'),
    path('post/', PostList.as_view(), name='post_list'),
    path('reply/', ReplyList.as_view(), name='reply_list'),
    path('replyadd/', ReplyAdd.as_view(), name='reply_add'),
    path('gamedata/', GameDataList.as_view(), name='game_data'),
    path('player/<int:pk>', PlayerDetails.as_view(), name='player_details'),
    path('post/<str:user>', PostDetail.as_view(), name='post_details'),
    path('reply/<int:pk>', ReplyDetail.as_view(), name='reply_details'),
    path('gamedata/<int:user_id>', GameDataDetail.as_view(), name='game_data_details'),
    path('api-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token-refresh/', TokenRefreshView.as_view(), name='token_refresh')
]