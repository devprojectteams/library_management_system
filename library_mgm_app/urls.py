from rest_framework.routers import DefaultRouter

from . import views
from django.urls import path, include

router = DefaultRouter()
router.register('authors', views.AuthorViewSet)
router.register('books', views.BookViewSet)

# urlpatterns = router.urls is for viewset and not for class

urlpatterns = [
    path('router/', include(router.urls)),
    # path('list_authors/', views.AuthorViewSet.as_view()),
    path('send_mail/', views.send_mail_function),
]
# urlpatterns = [
#     path('all_author/', views.all_author, name='home'),
#     path('authors/<int:pk>', views.AuthorDatailView.as_view(), name='author-detail'),
#     path('list_authors/', views.AuthorList.as_view()),
#     path('list_books/', views.all_books),
#     path('book_detail/<int:pk>/', views.book_detail),
#
#
#
#
#
#     # path('list_authors/', views.AuthorView.as_view()),
#     # path('welcome/', views.welcome),
# ]







# from django.http import HttpResponse
# from django.shortcuts import render, get_object_or_404
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter
# from rest_framework.generics import ListCreateAPIView
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework.views import APIView
# from rest_framework.viewsets import ModelViewSet
#
# from .filter import AuthorFilter, BookFilter
# from .models import Author, Book
# from .pagination import DefaultPagination
# from .serializers import AuthorSerializer, BookSerializer
# from rest_framework import status
#
#
# # Create your views here.
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # from django.urls import path, include
# # from rest_framework.routers import SimpleRouter, DefaultRouter
# #
# # from . import views
# #
# # # router = SimpleRouter()
# # router = DefaultRouter()
# # router.register('authors', views.AuthorViewSet)
# # router.register('books', views.BookViewSet)
# # urlpatterns = router.urls
#
# # print(router.urls)
# #
# # urlpatterns = [
# #     path('', include(router.urls)),
#     # path('authors/', views.list_authors),
#
#     # class component
#
#     # path('welcome', views.welcome),
#     # path('me/', views.last_name),
#     # path('authors/', views.list_authors),
#     # path('authors/<int:pk>/', views.author_detail, name='author-detail'),
#
#     #  CLASS COMPONENT FOR BOOKS
#
#     # path('book/<int:pk>/', views.BookDetail.as_view()),
#     # path('books/', views.BookList.as_view())
#
# # ]
#
#
#
#
#
#
#
#
#
#
#
#
#
# # urlpatterns = [
# #     path('',include((router.urls)),
# #        path('authors/', AuthorList.as_view())
# #     # path('authors/', views.find_all_author),
# #     path('authors/', views.AuthorView.as_view()),
# #     path('welcome/', views.welcome),
# #     # path('authors/<int:pk>/', views.author_detail, name='author-detail'),
# #     path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
# #     path('books/<int:pk>/', views.book_detail, name='book-detail'),
# #     path('books/', views.find_all_books),
# #     path('__debug__/', include('debug_toolbar.urls')),
# # ]
