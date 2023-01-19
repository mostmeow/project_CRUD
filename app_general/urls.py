from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listitem', views.listitem, name='listitem'),
    path('taskcreate', views.taskcreate, name='taskcreate'),
    path('videoitem', views.videoitem, name='videoitem'),
    
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),

    path('createtest', views.createtest, name='createtest'),
]