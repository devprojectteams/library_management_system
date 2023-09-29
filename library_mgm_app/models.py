from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


# class Book(models.Model):
#     title = models.CharField(max_length=255)
#     author = models.ForeignKey('Author', on_delete=models.CASCADE)

# or

class User(AbstractUser):
    email = models.EmailField(unique=True)


class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=250, blank=False, null=False)
    email = models.EmailField(blank=True, default="")
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.date_of_birth} {self.email}"


class Book(models.Model):
    LANGUAGE_CHOICES = [
        ("Y", 'YORUBA'),
        ("H", 'HAUSA'),
        ("I", 'IGBO'),
        ("E", 'ENGLISH'),
    ]
    GENRE_CHOICES = [
        ("FIC", 'FICTION'),
        ("POL", 'POLITICS'),
        ("FIN", 'FINANCE'),
        ("ROM", 'ROMANCE'),
    ]

    title = models.CharField(max_length=255, blank=False, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=15, blank=False, null=False)
    description = models.CharField(max_length=300, blank=False, null=False)
    date_added = models.DateTimeField(blank=True, null=True)
    genre = models.CharField(max_length=15, choices=GENRE_CHOICES)
    language = models.CharField(max_length=15, choices=LANGUAGE_CHOICES, default="")
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.title} {self.author} {self.isbn} {self.price} {self.genre} {self.language}"


class Genre(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return f"{self.name}"


class Language(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"


class BookInstance(models.Model):
    STATUS_CHOICES = [
        ('AVAILABLE', 'A'),
        ('BORROWED', 'B')
    ]

    unique_id = models.UUIDField(primary_key=True, default=uuid4)
    due_back = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='A')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.STATUS_CHOICES} {self.due_back} {self.status} {self.unique_id} "
