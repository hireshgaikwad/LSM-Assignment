from email import message
import re
from unicodedata import category
from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def Indexpage(request):
    return render(request,"app/index.html")

def Adminlogin(request):
    email = request.POST['email']
    password = request.POST['password']

    if email == "admin@gmail.com" and password == "admin":

        request.session['email'] = email
        request.session['password'] = password
        return redirect('home')

    else:
        message = "Username and password not match"
        return render(request,"app/login.html",{'msg':message})

def SignupPage(request):
    return render(request, "app/signup.html")


def Register(request):
    if request.method == "POST":          
            email = request.POST['email']
            password = request.POST['password']
            cpassword = request.POST['cpassword']


            user = UserMaster.objects.filter(email=email)

            if user:
                message = "User already exists"
                return render(request,"app/signup.html",{'msg':message})

            else:
                if password == cpassword:
                    

                    newuser = UserMaster.objects.create(email=email,password=password)

                    

                    return render(request,"app/login.html",{'email':email})
                else:
                    message = "Password missmatch!!"
                    return render(request,"app/signup.html",{'msg':message})
    else:
        message = "Bad request"
        return render(request,"app.signup.html",{'msg':message})

def LoginPage(request):
    return render(request,"app/login.html")

def Homepage(request):
    return render(request,"app/home.html")

def Login(request):
    if request.method =="POST":
        email = request.POST['email']
        password = request.POST['password']


        user = UserMaster.objects.get(email=email)

        if user:
            if user.password==password:
                request.session['email'] = user.email
                request.session['password'] = user.password

                return render(request,"app/home.html")
            else:
                message = "Password Missmatch"
                return render(request,"app/login.html",{'msg':message})

        else:
            message = "User does not exists"
            return render(request,"app/login.html",{'msg':message})

    else:
        message = "Bad request"
        return render(request,"app.signup.html",{'msg':message})



def AddBookPage(request):
    return render(request,"app/addbook.html")

def Addbook(request):
    if request.method == "POST":
        name = request.POST['bname']
        author = request.POST['author']
        isbn = request.POST['isbn']
        category = request.POST['category']

        book = Book.objects.create(name=name,author=author,isbn=isbn,category=category)

        message = "Book Added Successfully!!"
        return render(request,"app/addbook.html",{'msg':message})
    else:
        message = "Bad Request"
        return render(request,"app/addbook.html",{'msg':message})

def ViewBooks(request):
    books = Book.objects.all()
    return render(request,"app/books.html",{'books':books})

def UpdateBook(request,pk):
    book = Book.objects.get(pk=pk)

    book.available = request.POST['available']
    book.save()
    print("Book Updated")
    return render(request,"app/books.html")

def BookDelete(request,pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('viewbook')

def logout(request):
    del request.session['email']
    del request.session['password']
    return redirect('index')

###############################################
##########STUDENT LOGIN########################
def StudentLoginPage(request):
    return render(request,"app/studlogin.html")

def StudentHome(request):
    return render(request,"app/student_home.html")

def StudentLogin(request):
    if request.method =="POST":
        email = request.POST['email']
        password = request.POST['password']


        user = UserMaster.objects.get(email=email)

        if user:
            if user.password==password:
                request.session['email'] = user.email
                request.session['password'] = user.password

                return render(request,"app/student_home.html")
            else:
                message = "Password Missmatch"
                return render(request,"app/login.html",{'msg':message})

        else:
            message = "User does not exists"
            return render(request,"app/login.html",{'msg':message})

    else:
        message = "Bad request"
        return render(request,"app.signup.html",{'msg':message})

def ViewBooks1(request):
    books = Book.objects.all()
    return render(request,"app/books1.html",{'books':books})



