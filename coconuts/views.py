from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse


def root(request):
    return redirect("/blogs")
# Create your views here.


def index(request):
    # return render(request, "index.html")
    return HttpResponse("placeholder to display a list of blogs")


def new(request):
    return HttpResponse("placeholder to display a new form to make a blog")


def create(request):
    return redirect("/")


def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")


def edit(request, number):
    return HttpResponse(f"placeholder to edit blog number: {number}")


def destroy(request, number):
    return redirect("/blogs")


def bonus(request):
    return JsonResponse({"title": "this is a title", "content": "we could put content here"})