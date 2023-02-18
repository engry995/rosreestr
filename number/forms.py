from django import forms
from django.core.validators import FileExtensionValidator
from django.forms import DateInput


from .models import BaseObject


class NumberForm(forms.Form):
    file = forms.FileField(label='Загрузить файл',
                           help_text='Выберите файл .txt',
                           validators=[FileExtensionValidator(['txt'], message='Файл должен быть TXT формата!')])
    type_of_object = forms.ChoiceField(label='Тип загружаемых значений', choices=BaseObject.TYPE_OBJECT_CHOICES)


class DateInputWidget(DateInput):
    input_type = 'date'


class DateForm(forms.Form):
    date = forms.DateField(label='Выберите дату', widget=DateInputWidget())
