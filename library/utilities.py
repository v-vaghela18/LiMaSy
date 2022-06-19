import datetime
from django.utils import timezone
from .models import Book, Issue
from Reader.models import Reader

def getmybooks(user):
    requestedbooks=[]
    issuedbooks=[]
    if user.is_authenticated:
        reader=Reader.objects.filter(reader_id=user)
        if reader:
            for b in Book.objects.all():
                for i in b.issue_set.all():
                    if i.reader==reader[0]:
                        if i.issued:
                            issuedbooks.append(b)
                        else:
                            requestedbooks.append(b)
    return[requestedbooks,issuedbooks]
