from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # < Import these
from .models import Book
from .forms import BookForm


def list_books(request):
    query = request.GET.get('q')
    if query:
       books = Book.objects.filter(Q(name__contains=query))
    else:
       books = Book.objects.all()

    # Pagination
    paginator = Paginator(books, 5)
    page = request.GET.get('page')

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'books.html', {'books': books, 'page': page})


def create_book(request):
    form = BookForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_books')

    return render(request, 'books-form.html', {'form': form})


def update_book(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect('list_books')

    return render(request, 'books-form.html', {'form': form, 'book': book})


def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()

    return redirect('list_books')

