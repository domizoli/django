from django.shortcuts import render
from . models import cv_user
from django.contrib.auth import views

def cv(request):
   context = {}

   # cv = cv_user.objects.filter(name="Zoltan Domonkos")
   cv = cv_user.objects.all()
   context['cv_user'] = cv
   return render(request, 'cv.html', context)

def main(request):
   return render(request, 'main.html')

def newuser(request):
   users = cv_user.objects.all()
   count = cv_user.objects.all().count()
   if request.method == "GET":
      return render(request, 'newuser.html', {"users": users, "count": count})
   elif request.method == "POST":
     name = request.POST.get('name')  
     email = request.POST.get('email')

   saveuser = cv_user.objects.create(name=name, email=email)
   saveuser.save

   return render(request, 'newuser.html', {"users": users, "count": count})