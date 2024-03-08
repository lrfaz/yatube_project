# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse('My first page')


def group_posts(requst, slug):
    return HttpResponse("You can see here post")
