from django.shortcuts import redirect, render
from django.contrib import messages
from . models import User, UserManager
import bcrypt

# Create your views here.
def index(request):
    return render(request, "login.html")

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request, "success.html")

def register(request):
    ## Crear user
    if request.method =='POST':
        ## Validar los datos
        errors= User.objects.validator(request.POST)
        if errors:
            for error in errors.values():
                messages.error(request, error)
            return render(request, 'login.html')
        ## encriptando pw
        #almacenando texto plano en variable
        user_pw= request.POST['pw']
        #hashear las contraseña
        hash_pw=bcrypt.hashpw(user_pw.encode(), bcrypt.gensalt()).decode()
        # test de hash
        print(hash_pw)
        new_user= User.objects.create(first_name=request.POST['f_name'], last_name=request.POST['l_name'],
        email=request.POST['email'], password=hash_pw)
        print(new_user)
        request.session['user_id']=new_user.id
        request.session['user_name']=f"{new_user.first_name} {new_user.last_name}"
        return redirect('/success')
    return redirect('/')

def login(request):
    if request.method=='POST':
        #consukta oara usuarios loggeados
        logged_user=User.objects.filter(email=request.POST['email'])
        if logged_user:
            logged_user=logged_user[0]
            #comparar las contraseñas
            if bcrypt.checkpw(request.POST['pw'].encode(), logged_user.password.encode()):
                request.session['user_id']=logged_user.id
                request.session['user_name']=f"{logged_user.first_name} {logged_user.last_name}"
                return redirect('/success')
    return redirect('/')