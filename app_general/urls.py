from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listitem', views.listitem, name='listitem'),
    path('userform', views.userform, name='userform'),
    path('videoitem', views.videoitem, name='videoitem'),
    
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
]