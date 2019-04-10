from django.shortcuts import render, HttpResponse, redirect
from .forms import AddBookForm,SearchBookForm,SearchBookFormA
from .models import Stock

# Create your views here.
def index(request):
    #print(request.session.get('first_name'))
    return render(request, 'Bookstore/index.html')
def shelf(form_data):
    if form_data["book_cat"] == "EDUCATION":
        return 1
    elif form_data["book_cat"] == "NOVEL":
        return 2
    elif form_data["book_cat"] == "POETRY":
        return 3
    elif form_data["book_cat"] == "DRAMAS":
        return 4
    else:
        return 5
    
def add_book(request):
    my_form = AddBookForm()
    data = ""
    if request.method == "POST":
        my_form = AddBookForm(request.POST)
        if my_form.is_valid():
            form_data = my_form.cleaned_data
            shelf_no = shelf(form_data)
            form_data["shelf_no"] = shelf_no
            Stock.objects.create(**form_data)
            #s = Stock(**my_form.cleaned_data)
            #s.save()
            return redirect('addbook_response')
    context = {
        "form" : my_form,
        "data" : data
    }
    return render(request, 'Bookstore/add_book.html', context)

def add_book_response(request):
    return render(request, 'Bookstore/add_book_response.html')

def search_book(request):
    my_form = SearchBookForm()
    data = []
    if request.method == "POST":
        my_form = SearchBookForm(request.POST)
        if my_form.is_valid():
            b_name = my_form.cleaned_data["book_name"]
            data_list = Stock.objects.filter(book_name = b_name)
            #print(data_list["book_name"])
            my_form = SearchBookForm()
            context={
                "form" : my_form,
                "data" : data_list
            }
            return render(request, 'Bookstore/search_book.html', context)
    context = {
        "form" : my_form,
        "data" : data
    }
    return render(request, 'Bookstore/search_book.html', context)

def search_book_auth(request):
    my_form = SearchBookFormA()
    data = []
    #request.session['first_name'] = 'swain'
    if request.method == "POST":
        my_form = SearchBookFormA(request.POST)
        if my_form.is_valid():
            b_name = my_form.cleaned_data["author_name"]
            data_list = Stock.objects.filter(book_auth = b_name)
            my_form = SearchBookFormA()
            context={
                "form" : my_form,
                "data" : data_list
            }
            return render(request, 'Bookstore/search_book_auth.html', context)
    context = {
        "form" : my_form,
        "data" : data
    }
    return render(request, 'Bookstore/search_book_auth.html', context)

def cart_home(request, id):
    if id != 0:
        data_list = Stock.objects.get(id = id)
        context = {
            "data" : data_list
        }
        data_list.book_qty = data_list.book_qty - 1
        data_list.save()
        return render(request, 'Bookstore/cart.html', context)
    else:
        data = []
        context = {
            "data" : data
        }
        return render(request, 'Bookstore/cart.html', context)

def analytics(request):
    return render(request, 'Bookstore/analytics.html', {})