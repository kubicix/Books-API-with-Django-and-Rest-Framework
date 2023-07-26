from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Book
from api.serializer import BookSerializer
from rest_framework import status

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def book(request,id):
    try:
        book = Book.objects.get(pk=id)
        serializer =BookSerializer(book)
        return Response(serializer.data)
    except:
        return Response({"error":"There is no matching data"},status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)