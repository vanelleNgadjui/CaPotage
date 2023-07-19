from django.urls import path ,re_path
from .consumers import ChatConsumer, CommentConsumer


websocket_urlpatterns = [
	path("<room_slug>" , ChatConsumer.as_asgi()) ,
    re_path(r'^ws/(?P<room_slug>[^/]+)/$', ChatConsumer.as_asgi()),
    re_path(r'^ws/ventes/comments/(?P<vente_id>\d+)/$', CommentConsumer.as_asgi()),
]
