from django.urls import path
from . import views

app_name = "content"

urlpatterns = [
    path('', views.homepage, name='home'), # HOME
    path('info/', views.info, name='info'), # LEARN MORE 
    path('posts/', views.posts, name='posts'), # ELENCO E CREAZIONE POST 
    path('posts_mng/', views.posts_mng, name='posts_mng'), # GESTIONE POST 
    path('post/<int:id>/', views.post_detail, name='post_detail'), # DETTAGLIO POST 
    path('user/<int:id>/', views.user_id, name='user_id'), # USER E CORRISPONDENTE ID
    path('APIs/', views.APIs, name='APIs'), # ELENCO ENDPOINTS API
    path('api/1h/', views.api_posts_1h, name='api_posts_1h'), # ENDPOINT PER 1H 
    path('api/<str:str>/', views.api_posts_str, name='api_posts_str'), # ENDPOINT PER RICERCA DI UNA STRINGA 
]
