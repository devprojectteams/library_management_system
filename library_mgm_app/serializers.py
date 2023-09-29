from decimal import Decimal

from djoser.serializers import UserCreateSerializer as BasedUserCreateSerializer
from djoser.serializers import UserSerializer as BasedCurrentUserSerializer
from rest_framework import serializers

from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth', 'email']
    # first_name = serializers.CharField(max_length=255)
    # last_name = serializers.CharField(max_length=255)
    # date_of_birth = serializers.DateField()


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'language', 'genre', 'book_number', 'discount_price']

    # author = serializers.HyperlinkedRelatedField(
    #     queryset=Author.objects.all(),
    #     view_name='author-detail')
    book_number = serializers.CharField(max_length=15, source='isbn')
    discount_price = serializers.SerializerMethodField(method_name='calculate')

    # title = serializers.CharField(max_length=250)
    # author = serializers.CharField(max_length=50)
    # price = serializers.DecimalField(max_digits=6, decimal_places=2)

    def calculate(self, book: Book):
        return book.price * Decimal(0.1)


class UserCreateSerializer(BasedUserCreateSerializer):
    class Meta(BasedUserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']


class UserSerializer(BasedCurrentUserSerializer):
    class Meta(BasedCurrentUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']

# from decimal import Decimal
#
# from rest_framework import serializers
#
# from .models import Author, Book
# from .serializer import serializers
#
#
# class AuthorSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Author
#         fields = ['first_name', 'last_name', 'email', 'date_of_birth']

# first_name = serializers.CharField(max_length=300)
# last_name = serializers.CharField(max_length=300)
# email = serializers.EmailField()
# date_of_birth = serializers.DateField()

#
# class BookSerializer(serializers.ModelSerializer):
#     # author = AuthorSerializer()
#
#     class Meta:
#         model = Book
#         fields = ['title', 'book_number', 'description', 'date_added', 'language', 'genre', 'discount_price', 'author']
#
#         author = serializers.HyperlinkedRelatedField(
#             queryset=Author.objects.all(),
#             view_name='author-detail'
#         )
#
#     book_number = serializers.CharField(max_length=20, source='isbn')
#     discount_price = serializers.SerializerMethodField(method_name='calculate')
#
#     def calculate(self, book: Book):
#         return book.price * Decimal(0.1)

# title = serializers.CharField(max_length=300)
#
# isbn = serializers.CharField(max_length=13)
# description = serializers.CharField(max_length=300)
# date_added = serializers.DateTimeField()
# language = serializers.CharField(max_length=15)
# genre = serializers.CharField(max_length=10)
# price = serializers.DecimalField(max_digits=6, decimal_places=2)


# from decimal import Decimal
#
# from rest_framework import serializers
#
# from book.models import Author, Book
#
#
# # class AuthorSerializer(serializers.Serializer):
# #     first_name = serializers.CharField(max_length=255)
# #     last_name = serializers.CharField(max_length=255)
# #     date_of_birth = serializers.DateField()
#
#
# # class BookSerializer(serializers.Serializer):
# #     title = serializers.CharField(max_length=255)
# #     genre = serializers.CharField(max_length=15)
# #     language = serializers.CharField(max_length=15)
# #     price = serializers.DecimalField(max_digits=6, decimal_places=2)
# #     description = serializers.CharField(max_length=300)
# #     # book_number = serializers.CharField(max_length=15, source='isbn')
# #     # author = serializers.ForeignKey(Author)
#
#
# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = ['first_name', 'last_name', 'date_of_birth']
#
#
# class BookSerializer(serializers.ModelSerializer):
#     # author = AuthorSerializer()
#
#     class Meta:
#         model = Book
#         fields = ['title', 'genre', 'language', 'price', 'description', 'book_number', 'discount_price']
#         #  'to display all the fields' fields = '__all__'
#
#     # author = serializers.HyperlinkedRelatedField(
#     #     queryset=Author.objects.all(),
#     #     view_name='author-detail'
#     # )
#
#     book_number = serializers.CharField(max_length=15, source='isbn')
#     discount_price = serializers.SerializerMethodField(method_name='calculate')
#
#     def calculate(self, cost: Book):
#         return cost.price * Decimal(0.1)
