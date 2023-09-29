from django.shortcuts import render
from django.http.response import JsonResponse


def links(request):
    context = {}
    return render(request, "home.html", context)
