from django.shortcuts import render
from resume import views


# def cv(request):
#    datas = {
#    'name':       'Zoltan Domonkos',
#    'birthdate':  '1981.04.07.',
#    'email':      'zoltan.g.domonkos@gmail.com',
#    'phone':      '+502 5866 1532',
#    'address':    'San Bartolomé Milpas Altas, Guatemala',
#    'linkedin':   'www.linkedin.com/in/domonkos-zoltan'
#    }
#    return render(request, 'cv.html', {'datas': datas})

def main(request):
   return render(request, 'main.html')