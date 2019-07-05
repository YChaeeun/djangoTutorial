from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResonse("hello, world")

def post_list(request):
    return render(request, 'blog/post_list.html',{})
