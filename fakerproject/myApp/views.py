from django.shortcuts import render
from myApp.models import Student
from django.db.models import Max
# Create your views here.
def view1(request):
    s=Student.objects.all()
    d={"stud":s}
    print(s)
    return render(request,'myApp/1.html',d)
