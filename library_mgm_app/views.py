from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse, BadHeaderError
from templated_mail.mail import BaseEmailMessage
from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, IsAdminUser
from .filter import AuthorFilter, BookFilter
from .models import Author, Book
from .pagination import DefaultPagination
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import status


# Create your views here.
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = AuthorFilter
    search_fields = ['first_name', 'last_name']
    permission_classes = [DjangoModelPermissions]
    # permission_classes = [IsAuthenticated]


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BookFilter
    search_fields = ['title']
    permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticated]


#
class AuthorList(ListCreateAPIView):
    def get_queryset(self):
        return Author.objects.all()


class AuthorView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializers = AuthorSerializer(authors, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("SUCCESS", status=status.HTTP_201_CREATED)


# function base view, classbased view, viewset in pythons
# def send_mail_function(request):
#     try:
#         send_mail("library message", "Your book order is now available", "timothy2@gmail.com",
#               ["fakemail@gmail.com", "ojo@gmail.com"])
#     except BadHeaderError:
#         pass
#     return HttpResponse('ok sent')
#

# class using EmailMessage
# def send_mail_function(request):
#     try:
#         message = EmailMessage("library message", "Your book order is now available", "timothy2@gmail.com",
#                                ["fakemail@gmail.com", "ojo@gmail.com"])
#         message.attach_file('library_mgm_app/static/images/chatwavelogo.png')
#         message.send()
#     except BadHeaderError:
#         pass
#     return HttpResponse('ok sent')


def send_mail_function(request):
    try:
        # sending Html messages with app name
        message = BaseEmailMessage(
            context={"name": "Asa"},
            template_name='library_mgm_app/email.html')
        message.send(to=["pauline@gmail.com"])
    except BadHeaderError:
        pass
    return HttpResponse('ok sent')

# class BookList(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     def get_serializer_context(self):
#       return {"request": self.request}
#
#
# class BookDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# @api_view()
# def list_books(request):
#     books = Book.objects.all()
#     serializers = BookSerializer(books, many=True, context={'request': request})
#     return Response(serializers.data, status=status.HTTP_200_OK)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def book_detail(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'GET':
#         book = Book.objects.get(pk=pk)
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
#     elif request.method == 'PUT':
#
#         serializer = BookSerializer(book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         serializer.save()
#
#         return Response("detail updated", status=status.HTTP_200_OK)
#
#     elif request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
