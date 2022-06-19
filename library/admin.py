from django.contrib import admin
import datetime
from django.utils import timezone
from .models import Author,Book,Issue
# Register your models here.



@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display=('reader','book','issued','returned')
    list_filter=('issued','returned')
    fields=('reader','book',('issued','returned'),'issued_at','return_date')
    search_fields=['reader__reader_id__username','book__name']
    autocomplete_fields = ['reader','book']
    list_per_page=30






@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('name','author','category')
    search_fields=['name','category']
    list_filter = (
        ('author', admin.RelatedOnlyFieldListFilter),
    )
    list_per_page=30



class BookInline(admin.TabularInline):
    model = Book

class IssueInline(admin.TabularInline):
    model = Issue
    extra=0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=['name']
    inlines = [
        BookInline,
    ]
    list_per_page=30
