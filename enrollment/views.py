from django.shortcuts import render,HttpResponseRedirect
from .models import Student
from .forms import StudentResgistration
# Create your views here.

def add_show(request):
    """ This function is used for to add student data in a database """
    if request.method == 'POST':
        fm = StudentResgistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['password']
            reg = Student(name=nm,email=em,password=ps)
            reg.save()
            fm = StudentResgistration()
    else:
        fm = StudentResgistration()

    std_data = Student.objects.all()
    return render(request,'enrollment/add_showStudent.html',{'form':fm ,'std':std_data })

def update(request,id):
    if request.method == 'POST':
        update = Student.objects.get(pk=id)
        fm = StudentResgistration(request.POST,instance=update)
        if fm.is_valid():
            fm.save()
    else:
        update = Student.objects.get(pk=id)
        fm = StudentResgistration(instance=update)
        return render(request,'enrollment/update.html',{'form':fm}) 
    return HttpResponseRedirect('/')
    


def delete_data(request,id):
    if request.method == 'POST':
        d = Student.objects.get(pk=id)
        d.delete()
        return HttpResponseRedirect('/')