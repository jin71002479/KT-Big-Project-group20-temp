from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here.

def index(request):
    contact_list = Contact.objects.order_by('-contact_pub_date')
    result = [ c.contact_title for c in contact_list ]
    return HttpResponse( str(result) )