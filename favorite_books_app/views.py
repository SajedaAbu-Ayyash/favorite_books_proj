from django.shortcuts import render, redirect

from . import models


# this function will render to root route, Registration/Login page
def index(request):
    return render(request, 'index.html')


# this function for registration
def register(request):
    models.register(request)
    return redirect('/')

#this function for login
def log_in(request):
    models.log_in(request)
    return redirect('/addbook')

#this function to success login and display all info in page
def success(request):
    if 'user_id' in request.session:
        context = {
            'books': models.Book.objects.all(),
            'users': models.User.objects.get(id = request.session['user_id'])
        }
        return render(request, "addbook.html", context)
    else:
        return redirect('/')

#this function for logout
def log_out(request):
    request.session.clear()
    return redirect('/')

#this function to create book
def add_book(request):
    models.add_book(request)
    return redirect('/addbook')

#this function to display book details
def show_book_details(request, book_id):
    context = {
        'books': models.Book.objects.all(),
        'users': models.User.objects.get(id = request.session['user_id'])
    }
    return render(request, 'bookdetails.html', context)

#this function to add to favbook
def favorite_book(request, book_id):
    models.favorite_book(request.session['id'], book_id)
    return redirect('/addbook')

#this function to edit book
def edit_book(request, book_id):
    context = {
        'books': models.Book.objects.get(id = book_id),
        'users': models.User.objects.get(id = request.session['user_id'])
    }
    if request.method == 'POST':
        edit_book(book_id, request.POST)
    return render(request, 'updatebook.html', context)
    
#this function to delete book
def delete_book(request):
    models.delete_book(request)
    return redirect('/addbook')
    

# Create your views here.