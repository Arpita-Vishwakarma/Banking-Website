#from django.contrib.auth import get_user_model
#from django.shortcuts import render, HttpResponse
#from django.template import loader
#from .forms import UserForm
#from .models import User
#from django.shortcuts import redirect


#Creating the objects of record

from django.shortcuts import render
from django.contrib.auth import get_user_model

def home(request):
    User = get_user_model()
    users = User.objects.all()
    
    return render(request, 'index.html', {'users': users})
