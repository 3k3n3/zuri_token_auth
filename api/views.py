from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse


def links(request):
    """URLS for Task."""
    body = f"""
    <h2>Token Authentication System</h2>
    <a href="#">Documentation</a><br>
    <a href="https://github.com/3k3n3/zuri_getpost">GitHub</a><br>
    <a href="#">Get</a><br>
    <a href="#">Post</a> <br>
    """
    return HttpResponse(body)
