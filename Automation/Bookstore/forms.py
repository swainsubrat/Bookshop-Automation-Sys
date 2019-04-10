from django import forms

class AddBookForm(forms.Form):
    book_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Book Name"
            }
        ), max_length=30, label = 'Book Name'
        )
    book_cat = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Category"
            }
        ), label='Book Category', max_length=30)
    book_auth = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Author"
            }
        ), label='Book Author', max_length=30)
    book_pub = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Publication"
            }
        ), label='Book Publication', max_length=30)
    book_price = forms.FloatField(
        widget = forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Price"
            }
        ), label='Book Price', min_value=1)
    book_qty = forms.IntegerField(
        widget = forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Nos of copies"
            }
        ), label='Book Quantity', min_value=1)

class SearchBookForm(forms.Form):
    book_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Book Name"
            }
        ),label='Book Name:', max_length=30)

class SearchBookFormA(forms.Form):
    author_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Book Author"
            }
        ),label='Book Author:', max_length=30)