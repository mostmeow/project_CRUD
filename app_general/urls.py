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

    # name is all auth package setup
    path('sociallogin', views.sociallogin, name='account_login'),

    path('createtest', views.createtest, name='createtest'),

    path('testsend', views.testsend, name='testsend'),
    path('testget/<str:data>', views.testget, name='testget'),


]