from django.shortcuts import render
from . models import Contact,User
from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *

# Create your views here.
def index(request):
    try:
        request.session['password']
        return redirect('login')
    except:
        img = Person.objects.all()
        return render(request,'index.html')

def contact(request):
    if(request.method =='POST'):
        obj = Contact.objects.create(
            name = request.POST.get('txtName'),
            email = request.POST.get('txtEmail'),
            phno = request.POST.get('txtPhone'),
            message = request.POST.get('txtMsg'),
        )
        obj.save()
        return redirect('index')
    else:    
        return render(request,'contact.html') 

def login(request):
    try:
        img = Person.objects.all()
        image = []
        for i in range(0,len(img)):
            image.append(img[i].image)  
        password = request.session['password']
        obj = User.objects.get(user_password=password)
        context = {'name':obj.user_name,'img':image}
        return render(request,'index.html',context)
    except:
        if(request.method == 'POST'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                obj = User.objects.get(user_name=username,user_password=password)
                request.session['password'] = password
                return redirect('login')
            except:
                return render(request,'login.html',{'msg':'Invalid Username or Password'})
        else:
            return render(request,'login.html')  


def register(request):
    if(request.method =='POST'):
        try:
            obj = User.objects.create(
                user_name = request.POST.get('name'),
                user_phno = request.POST.get('phno'),
                user_email = request.POST.get('email'),
                user_password = request.POST.get('psw')
            )
            obj.save()
            return redirect('login')
        except:
            return HttpResponse('<h1>Password already available; Please Change your Password</h1>')
    else:
        return render(request,'register.html')            
              


def logout(request):
    try:
        del request.session['password']
    except:
        pass            
    return redirect('login')   

def post(request):
    return redirect('index')                   
             

def imageupload(request): 

	if request.method == 'POST':
            print(request.POST)
            form = ImageForm(request.POST, request.FILES) 

            if form.is_valid(): 
                form.save()
                return redirect('index') 
	else: 
		form = ImageForm() 
	return render(request, 'imageupload.html', {'form' : form})  
