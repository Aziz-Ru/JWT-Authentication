from django.shortcuts import render


def Home_View(request):
    return render(request,'home.html')
    