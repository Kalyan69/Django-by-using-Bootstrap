from django.shortcuts import render

# Create your views here.
def husband(request):
    n='https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css'
    e='kalyansinha04@gmail.com'
    return render(request,'husband.html',{"f":n,"email":e})

def wife(request):
    n='How are you my love'
    return render(request,"wife.html",{"f":n})