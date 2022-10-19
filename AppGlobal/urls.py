from django.urls import path
from AppGlobal.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('home', home),
    path('about/',about),
    path('login/', login_request),
    path('perfil/',perfil),
    path('registro/',registro),
    path('logout/', LogoutView.as_view(template_name = 'home.html'), name="Logout" ),
    path('perfil/changeAvatar/', agregarAvatar),
    path('perfil/editarPerfil/', editarPerfil),
    path('perfil/password/', password),
    path('inbox', Inbox, name='inbox'),
    path('directs/<username>', Directs, name='directs'),
   	path('new/', UserSearch, name='usersearch'),
   	path('new/<username>', NewConversation, name='newconversation'),
   	path('send/', SendDirect, name='send_direct'),
    path("add_blogs/",add_blogs),
    path("edit_blog_post/<str:slug>/", UpdatePostView.as_view(), name="edit_blog_post"),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('perfil/mis_blogs/', mis_blogs),
    path('delete_blog/<str:slug>/', DeleteBlogView.as_view(), name="delete_blog")

]