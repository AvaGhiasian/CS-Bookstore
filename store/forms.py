from django import forms

from store.models import Review


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