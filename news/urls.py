from django.urls import path
from .views import *

urlpatterns = [
    path('authorlist/', AuthorList.as_view()),
    path('news/', PostList.as_view()),
    path('news/<int:pk>', Post.as_view()),
]
