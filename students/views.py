from django.shortcuts import render

#Home view for portal
def home(request):
    return render(request, 'students/home.html')

#About view for portal 
def about(request):
    return render(request, 'students/about.html')