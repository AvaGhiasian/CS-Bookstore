from django import forms

from store.models import Author, Category, Review, Book, Image


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'body']
        widgets = {
            'rating': forms.Select(choices=[(i, f'{i} ⭐') for i in range(1, 6)]),
            'body': forms.Textarea(attrs={'rows': 4, 'placeholder': 'نظر خود را بنویسید...'}),
        }


class SearchForm(forms.Form):
    query = forms.CharField()


# only admin can access these forms to fill the DB using UI
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = 'created_at', 'updated_at'


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
