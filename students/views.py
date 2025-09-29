from django.shortcuts import render

#Home view for portal
def home(request):
    return render(request, 'students/home.html')

