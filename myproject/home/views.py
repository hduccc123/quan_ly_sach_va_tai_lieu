from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import render, get_object_or_404
# Create your views here.
def indexin(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request,'home/indexin.html', context)
def list_book(request):
    context = {}
    return render(request ,'home/list_book.html', context)
def list_doc(request):
    context = {}
    return render(request ,'home/list_doc.html', context)
def read_online(request, pk):
    books = Book.objects.get(pk=pk)
    context = {'books': books}
    return render(request, 'home/description.html',context)
def book_category(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'home/book.html', context)
def doc_category(request):
    docs = Doc.objects.all()
    context = {'docs': docs}
    return render(request,'home/doc.html', context)
def read_book_online(request, pk):
    books = get_object_or_404(Book, pk=pk)
    print("PDF URL:", books.books_pdf_url)
    return render(request, 'home/book_online.html', {'books': books})
def read_doc_online(request, pk):
    docs = get_object_or_404(Doc, pk=pk)
    return render(request, 'home/read_online.html', {'docs': docs})
def login(request):
    context = {}
    return render(request, 'home/login.html',context)
def register(request):
    context = {}
    return render(request, 'home/register.html', context)