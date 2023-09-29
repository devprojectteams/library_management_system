from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BasedUserAdmin
from library_mgm_app.models import Author
from .models import Book, BookInstance, User


# Register your models here.


@admin.register(User)
class UserAdmin(BasedUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "email", "first_name", "last_name"),
            },
        ),
    )


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_filter = ['email']
    list_per_page = 10


@admin.register(Book)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'genre', 'language']
    list_filter = ['author']
    list_per_page = 10

    @admin.register(BookInstance)
    class BookInstanceAdmin(admin.ModelAdmin):
        list_display = []

    # admin.site.register(Author, AuthorAdmin)
    # admin.site.register(Book)
    # admin.site.register(BookInstance)

    # admin.site.register(Author)
    # admin.site.register(Book)
