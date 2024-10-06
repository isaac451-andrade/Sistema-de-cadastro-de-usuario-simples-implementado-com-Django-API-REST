from django.shortcuts import render
from django.http import HttpResponse
from api_rest import models
def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == 'POST':
        user_nickname = request.POST['user_nickname']
        users = models.User.objects.all()

        for user in users:
            if user.user_nickname == user_nickname:
                return HttpResponse("Nome de usuário já existe!")

        new_user = models.User(user_nickname=user_nickname, user_name=request.POST['user_name'], user_email=request.POST['user_email'], user_age=request.POST['user_age'])    
        
        new_user.save()

        return render(request, 'home.html')

