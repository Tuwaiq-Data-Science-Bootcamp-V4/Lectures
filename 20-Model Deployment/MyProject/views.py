from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def result(request):
    fname = request.GET['fname']
    lname = request.GET['lname']
    return render(request, 'result.html', {'result': [fname,lname]})