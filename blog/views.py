from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html', context={'title':'测试', 'welcome': 'Hello,world'})