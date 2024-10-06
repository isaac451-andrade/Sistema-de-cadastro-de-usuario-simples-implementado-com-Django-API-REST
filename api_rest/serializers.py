from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    # Qual modelo estou serializando para JSON e quais campos vão poder ser serializados e serem mandados para o front-end!
    # A api nesse caso vai devolver todos os dados do usuário para o front-end!
    class Meta:
        model = User
        fields = '__all__'
        

