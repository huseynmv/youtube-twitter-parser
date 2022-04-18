
from django.urls import path
from .views import index, logout
app_name = 'youtube_twitter'
urlpatterns = [

    path('', index, name='home' ),
    path('logout/', logout, name='logout')
]
