from django.shortcuts import render,HttpResponse,redirect
from todoapp.models import TaskList
from django.db.models import Q
# Create your views here.
def contact_page(request):

    return HttpResponse("<h1>Hello from Contact page!!!!</h1>")

def home_page(request):
    #print("Value:",request.user.is_authenticated)
  if request.user.is_authenticated:  
    #return redirect('/contact')
    q1=Q(is_active=1)
    q2=Q(user_id=request.user.id)
    #t=TaskList.objects.all() #select * from todoapp_tasklist
    t=TaskList.objects.filter(q1 & q2)
    #select * from todoapp_tasklist where is_active=1 and user_id=request.user_id

    #print(t)
    #for x in t:#[obj1,obj2,obj3,obj4 accessing each object] 
      #print(x)
      #print("ID:",x.id)
      #print("Title:",x.title)
      #print("Detai:",x.detail)
      #print("Due Date",x.due_dt)
      #print("completed",x.is_completed)
      #print("active",x.is_active)
      #print()
  
    context={}
    context['data']=t

    return render(request,'todoapp/dashboard.html',context)    
  else:
    return redirect(request,'/authapp/login')


def add_task(request):
    print("Method type:",request.method)#GET|POST

    if request.method=="POST":#GET==POST false| POST==POST=>True
      #fetch form data
      t=request.POST['title']
      d=request.POST['det']
      dt=request.POST['duedt']
      #print("Title:",t)
      #print("Details:",d)
      #print("Date:",dt)
      t=TaskList.objects.create(title=t,detail=d,due_dt=dt,user_id=request.user)#object created
      t.save()#object saved

      #return HttpResponse("Data inserted successfully into database table")

      #print("In if section")
      #return HttpResponse("Insert data into database")
      return redirect('/home')
    else:
      print("In else section")    
      return render(request,'todoapp/addtask.html')


def dtl(request):
  context={}
  context['a']=60
  context['user']="Raj"
  context['b']=80
  context['l']=[10,20,30,40,50,60]
  return render(request,'todoapp/dashboard.html',context)

def delete_task(request,rid):
  #print("ID to be deleted:",rid)
  #return HttpResponse("ID to be deleted:"+rid)
  #t=TaskList.objects.get(id=rid) #select * from tablename where id=3
  #print(t)
  #t.delete()
  #return HttpResponse("Record Fetched")
  #return HttpResponse("Object Deleted")
  t=TaskList.objects.filter(id=rid)
  t.update(is_active=0)
  return redirect('/home')

def edit_task(request,rid):
  #print("ID to be edited:",rid)
  #return HttpResponse("ID to be edited:"+rid) 

  if request.method=="POST":
    ut=request.POST['title']
    ud=request.POST['det']
    udt=request.POST['duedt']
    print("Updated Title:",ut)
    print("updated Details:",ud)
    print("updated date:",udt)
    t=TaskList.objects.filter(id=rid)
    t.update(title=ut,detail=ud,due_dt=udt)
    return redirect("/home")
    #return HttpResponse("Details Fetched")
  else:
    t=TaskList.objects.get(id=rid)#select * from todoapp_tasklist where id=3
    context={}
    context['data']=t
    return render(request,'todoapp/editform.html',context) 

def mark_completed(request,rid):
   t=TaskList.objects.filter(id=rid)#select * from todoapp_tasklist where id=8
   t.update(is_completed=1)

   return redirect('/home')    
       