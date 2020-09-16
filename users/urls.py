from django.urls import path
from .views import user_creation_view,user_profile_view,user_update_view,LoginViewClass,LogoutViewClass

urlpatterns = [

 
    path('',user_creation_view , name = 'usercreation' ),
    path('profile/',user_profile_view , name = 'profileview' ),
    path('profileupdate/',user_update_view , name = 'profileupdate' ),
    path('login/',LoginViewClass.as_view() , name='login'),
    path('logout/',LogoutViewClass.as_view() , name='logout'),
    
]