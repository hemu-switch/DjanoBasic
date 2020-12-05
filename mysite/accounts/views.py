from django.shortcuts import render, redirect

from django.contrib.auth.models import User, auth


def register(request):
    
    if request.method == 'POST':
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        first_name = request.POST['first_name']
        
        if password1 == password2 :
            user = User.objects.create_user(username=username, password=password1, email=email, first_name= first_name, last_name = last_name)
            user.save()
            print('User Created')
            return redirect('/')
        else:
            print('Password Not matchin')
    else:
    
        return render(request, 'register.html')

# Create your views here.
