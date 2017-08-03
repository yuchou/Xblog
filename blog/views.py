from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'blog/index.html', context={'title':'测试', 'welcome': 'Hello,world'})