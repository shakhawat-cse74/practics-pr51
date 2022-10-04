from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages
# Create your views here.
def showdata(request):
    if request.method == 'POST':
        fm= StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()
            messages.add_message(request,messages.INFO, 'Your account has been created successfully!!!')
            messages.success(request,'Now you are login')
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html',{'form':fm})