from django.shortcuts import render,redirect
from employeeapp.models import home as homes
import loginapp
# Create your views here.


def home(request):
    result = request.session.get('login')
    re = homes.objects.all()
    if result:
        return render(request,'emplist.html',{'re':re})
    return redirect('loginapp:login')



