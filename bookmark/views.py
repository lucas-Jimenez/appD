from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from bookmark.models import Bookmark
from bookmark.serializers import bookmarkSerializer
# Create your views here.

def bookmarkApi(request,id = 0):
    if request.method == 'GET':
        bookmarks = Bookmark.objects.all()
        bookmark_serializer = bookmarkSerializer(bookmarks,many=True)
        return JsonResponse(bookmark_serializer.data,safe=False)
    elif request.method == 'POST':
        bookmark_data = JSONParser().parse(request)
        bookmark_serializer = bookmark_serializer(data=bookmark_data)
        if bookmark_serializer.is_valid():
            bookmark_serializer.save()
            return JsonResponse("Added Succesfully", safe=False)
        return JsonResponse("Failed to add",safe = False)
    

