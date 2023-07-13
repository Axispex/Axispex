from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'axispex/index.html')


def loginpage(request):
    return render(request, 'axispex/loginpage.html')

def test(request):
    return render(request, 'axispex/test.html')