from django.urls import path
from blog.views import (post_create,post_list,Comment_Detail_View,
                        Comment_Form_View,DeletePost,search,
                        UpdatePost,Post_Comment_List,post_comment,Limited_PostDetail_User_View)
from django.contrib.auth import views
from django.views.generic import TemplateView
from django.views.decorators.http import  require_POST

urlpatterns = [
    path('postcreate/', post_create.as_view(),name='post_create'),
    path('', post_list.as_view(),name='post_list'),
    path('postcomment/', Post_Comment_List.as_view(),name='post_comment_list'),
    path('postcomment2/', post_comment.as_view(),name='post_comment'),
    path('post/<int:pk>', Comment_Detail_View.as_view(), name='post_detail'),
    path('delete/<int:pk>', DeletePost.as_view(), name='post_delete'),
    path('update/<int:pk>', UpdatePost.as_view(), name='post_update'),
    path('form/<int:pk>', require_POST(Comment_Form_View.as_view()), name='comment_form'),
    path('post1/<int:pk>', Limited_PostDetail_User_View.as_view(), name='detail1'),
    path('about/',TemplateView.as_view(template_name = 'blog/about.html'),name = 'about'),
    path('search/',TemplateView.as_view(template_name = 'blog/search.html'),name = 'search'),
    path('searchview',search,name='searchview'),
 
]

