from django.shortcuts import render

# Create your views here.
def docker(request):
    return render(request, "docker.html")