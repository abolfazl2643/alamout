from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apiapp import views

urlpatterns = [
    path('posts/', views.PostList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)