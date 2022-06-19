from django.urls import path
from .views import allbooks,search,sort,addbook,deletebook,issuerequest,myissues,issue_book,return_book,requestedissues

urlpatterns=[
    path('',allbooks, name='home'),
    path('search/', search),
    path('sort/', sort),
    path('addbook/', addbook),
    path('deletebook/<int:bookID>/', deletebook),
    path('request-book-issue/<int:bookID>/', issuerequest),
    path('my-issues/', myissues),
    path('issuebook/<int:issueID>/', issue_book),
    path('returnbook/<int:issueID>/', return_book),
    path('all-issues/', requestedissues),
]