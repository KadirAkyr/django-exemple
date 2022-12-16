from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.response import Response

# Create your views here.


def index(request):
    return HttpResponse('Hello World. You are at my app index')


class BookList(APIView):
    # List all books, or create a new book
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print("getOne function")
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data, safe=False)

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
