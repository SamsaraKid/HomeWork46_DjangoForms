from django import forms
import os

dir = os.getcwd()


class NashaForma(forms.Form):
    name = forms.CharField(label='Имя', initial='Имя')
    num = forms.IntegerField(label='Номер', required=False, max_value=100, initial=12, help_text='напишите число', disabled=True)


class AniForma(forms.Form):
    name = forms.CharField(label='Имя', initial='Барсик')
    breed = forms.CharField(label='Порода', initial='Кот')
    age = forms.IntegerField(label='Возраст', min_value=0, initial='5')
    color = forms.CharField(label='Цвет', initial='Рыжий')
    food = forms.CharField(label='Любимая еда', initial='Рыбовы')
    img = forms.ImageField(label='Фото')


