from django.shortcuts import render

# from CRUD_app.models import Task
from CRUD_app.models import Task

def index(request):
    if request.method =='POST':
        name =request.POST.get("name")
        username =request.POST.get("username")
        email =request.POST.get("mail")
        data =Task(Name =name,Username=username,Email =email)
        data.save()
        database_data =Task.objects.all()
        stu = {
              "student_number": database_data
            }
        return render(request,'index.html',stu)
        # normal route
    database_data =Task.objects.all()
    stu = {
        "student_number": database_data
            }  
    return render(request,'index.html',stu)    


def delete(request,Id):
    delete_data = Task.objects.get(Id=Id)
    delete_data.delete()
    database_data =Task.objects.all()
    stu = {
        "student_number": database_data
            }  
    return render(request,'index.html',stu)    
# Create your views here.
