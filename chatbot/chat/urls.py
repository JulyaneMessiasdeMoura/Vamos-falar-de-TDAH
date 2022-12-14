from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('ferramenta', views.ferramenta,name='ferramenta'),
    path('tdah',views.tdah,name='tdah'),
    path('ajuda',views.ajuda,name='ajuda'),
    path('referencias',views.referencias,name='referencias'),
    path('chat_enviar', views.chat_enviar, name='chat_enviar')
]