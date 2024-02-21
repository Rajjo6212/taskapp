from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def user_register(request):
    if request.method=="POST":
        #fetching data
        uname=request.POST['uname']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']
        uemail=request.POST['uemail']
        #validation of data
        context={}
        if uname=="" or upass=="" or ucpass=="" or uemail=="":
           context['errmsg']="Fields cannot be Blank"
           return render(request,"authapp/register.html",context)
        elif upass!=ucpass:
            context['errmsg']="Password and confirm Password Mismatch"
            return render(request,"authapp/register.html",context)
        else:
        #print("Username:",uname)
        #print("password:",upass)
        #print("Confirm Password:",ucpass)
        #print("email:",uemail)
          u=User.objects.create(username=uname,email=uemail)
          u.set_password(upass)#to store password in encrypted format in database
          u.save()

        #return HttpResponse("User created Successfully")
        #return redirect('authapp/login')
        context['success']="Account Created Successfully!!! Please login" 
        return render(request,"authapp/register.html",context)

    else:    
     return render(request,'authapp/register.html')

def user_login(request):     
    if request.method=="POST":
        uname=request.POST['uname']
        upass=request.POST['upass']
        print("username:",uname)
        print("password:",upass)

        u=authenticate(username=uname,password=upass)
        #print("User Object:",u)
        #print("ID:",u.id)
        #print("username:",u.username)
        #print("Password:",u.password)
        #print("Email:",u.email)
        #print("SuperUser:",u.is_superuser)
        #print("Datejoined:",u.date_joined)
        if u is not None:
            login(request,u)
            return redirect('/home') 
        else:
            context={}
            context['errmsg']="Invalid Username or Password" 
            return render(request,'authapp/login.html',context)
    else:
            return render(request,'authapp/login.html')

def user_logout(request):
    logout(request)#destroy data of the logged in user from session.
    return redirect('/authapp/login')        
   
         