from django.shortcuts import render

def blog_404(request):
    return render(request,"website/404.html")