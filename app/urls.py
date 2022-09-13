from django.urls import path
from . import views

urlpatterns = [
    path("",views.Indexpage,name='index'),
    path("adminlogin/",views.Adminlogin,name="adminlogin"),
    path("signup/",views.SignupPage,name="signup"),
    path("register/",views.Register,name="register"),
    path("loginpage/",views.LoginPage,name="loginpage"),
    path("home/",views.Homepage,name="home"),
    path("login/",views.Login,name="login"),
    path("addbookpage/",views.AddBookPage,name="addbookpage"),
    path("addbook/",views.Addbook,name="addbook"),
    path("bookview/",views.ViewBooks,name="viewbook"),
    path("delete/<int:pk>",views.BookDelete,name="delete"),
    path("update/<int:pk>",views.UpdateBook,name="update"),
    path("logout/",views.logout,name="logout"),

#####################################################################
    path("studhome/",views.StudentHome,name="studhome"),
    path("studloginpage/",views.StudentLoginPage,name="studloginpage"),

    path("studlogin/",views.StudentLogin,name="studlogin"),
    path("bookview1/",views.ViewBooks1,name="viewbook1"),


]