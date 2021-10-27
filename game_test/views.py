from django.shortcuts import render, redirect


def base(request):
    return render(request, 'game_test/base.html')

def index(request):
    print(request)
    return render(request, 'game_test/index.html')


