from fnmatch import translate
from django.shortcuts import render
from . models import cv_user, cv_user_education, cv_user_language, cv_user_work_expercience
from django.contrib.auth import views
from resume import views
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext

def cv(request):
   trans = translate(language='en')
   # trans = translate(language='es')
   # cv = cv_user.objects.filter(name="Zoltan Domonkos")
   # user_person = cv_user.objects.all()
   # user_education = cv_user_education.objects.all()
   # user_language = cv_user_language.objects.all()
   # user_work_expercience = cv_user_work_expercience.objects.all()
   # context={
   #       'user': user,
   #       'user_education': user_education,
   #       'user_language': user_language,
   #       'user_work_experience': user_work_expercience,
   #       }
   return render(request, 'cv.html', {'trans': trans})

def translate(language):
   cur_language = get_language()
   try:
      activate(language)
      # text = _('hello')
   finally:
      activate(cur_language)
      # text = gettext('hello')

def main(request):
   return render(request, 'main.html')

def newuser(request):
   pass
#    users = user.objects.all()
#    count = cv_user.objects.all().count()
#    if request.method == "GET":
#       return render(request, 'newuser.html', {"users": users, "count": count})
#    elif request.method == "POST":
#      name = request.POST.get('name')  
#      email = request.POST.get('email')

#    saveuser = cv_user.objects.create(name=name, email=email)
#    saveuser.save

#    return render(request, 'newuser.html', {"users": users, "count": count})
