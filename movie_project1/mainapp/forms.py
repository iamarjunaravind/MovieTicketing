from django import forms
from .models import Movie,Category

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['movie_name','movie_description','movie_category','movie_image','movie_price','shows','movie_date','movie_time']

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['category_name','category_description','category_image']