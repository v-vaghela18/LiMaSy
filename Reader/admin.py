from django.contrib import admin
from .models import Reader,City
from library.admin import IssueInline

from django.contrib.auth.models import User,Group
from django.contrib.auth.admin import UserAdmin


admin.site.unregister(User)
admin.site.unregister(Group)
class ReaderInline(admin.TabularInline):
    model = Reader
    # extra=0
# Register out own model admin, based on the default UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display=('username','reader','last_login')
    list_filter=('is_superuser','is_active')
    fieldsets =  (
      ('Standard info', {
          'fields': ('username','password',)
      }),
      ('Important Date & Time ', {
          'fields': ('last_login','date_joined',)
      }),)
    inlines = [
        ReaderInline
    ]
      
   


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    search_fields=['reader_id__username','first_name','city']
    fields=(('first_name','last_name'),('reader_id','city'))
    list_display=('first_name','last_name','reader_id','city')
    list_display_links = ('first_name', 'reader_id')
    list_filter=('city',)
    list_per_page=30
    inlines = [
        IssueInline
    ]
    
admin.site.register(City)