from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User
from .serializers import UserSerializer

@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()

        serializer = UserSerializer(users, many=True) # Pega todos os objetos e serializam para json, many é porque users é um QUERYSET

        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_by_nick(request, nick): # vou receber da url aqui dentro da função o nick!
    try:
        user = User.objects.get(pk=nick)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user) # pega o objeto user, transforma em json

        return Response(serializer.data)
    
@api_view(['GET', 'POST', 'PUT', 'DELETE']) # permite todos os tipos de requisição para a API
def user_manager(request):
    if request.method == 'GET':
        try:
            if request.GET['user']: # estou pegando o valor do parâmetro que estou passando na URL, ?user=user_nickname
                
                user_nickname = request.GET['user'] # armazena o valor do parâmetro na variável

                try:
                    user = User.objects.get(pk=user_nickname) # tenta achar o user pelo nickname

                    serializer = UserSerializer(user)

                    return Response(serializer.data)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':

        new_user = request.data # os dados que estão vindo do post

        serializer = UserSerializer(data=new_user)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)   

    if request.method == 'PUT':
        user_nickname = request.data['user_nickname']

        try:
            updated_user = User.objects.get(pk=user_nickname)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(updated_user, data=request.data) # nesse nickname, quero que vc atualize os dados para request.data

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':  
        try:
            user_to_delete = User.objects.get(pk=request.data['nick_name'])    
            user_to_delete.delete()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        