from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
import json

# restframework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication


from .serializers import TaskSerializer

# model
from app_general.models import TaskModel

from django.contrib.auth.models import User, Group

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>',

        'Createuser':'/user-create/',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = TaskModel.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    task = TaskModel.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    # ==GETD ATA==

    # --use Html form--
    # taskname = request.POST['taskname']
    # //

    # --use fetch json--
    # getdata = json.loads(request.body)
    # taskname = getdata['name']

    getdata = request.data
    taskname = getdata['name']
    # print(taskname)
    # //
    
    # ==PREPARE DATA==
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        # //       
        this_dict = serializer.validated_data
        this_dict['name'] = taskname

        print(this_dict)
        # //

        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    task = TaskModel.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = TaskModel.objects.get(id=pk)
    task.delete()

    return Response('Item Delete!')
