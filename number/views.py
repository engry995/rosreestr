from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.generic import TemplateView, FormView
from .forms import NumberForm, DateForm
from .services import get_numbers_from_file, add_numbers_to_base


class MainPage(TemplateView):
    template_name = 'main.html'


class LoadFile(FormView):
    template_name = 'load_file.html'
    form_class = NumberForm

    def form_valid(self, form):

        file = form.cleaned_data['file']
        type_of_object = form.cleaned_data.get('type_of_object')

        number = get_numbers_from_file(file)
        add_numbers_to_base(number, type_of_object)
        count_all = len(number)


        message = f'Загружены номера из файла {file.name}\n' \
                  f'Всего найдено номеров - {count_all}\n'
        return render(self.request, 'message.html', context={'message': message})


class EmailHandler(FormView):
    template_name = 'email_handler.html'
    form_class = DateForm

    def form_valid(self, form):

        date = form.cleaned_data.get('date')

        message = f'Обработаны письма за {date}\n'
        return render(self.request, 'message.html', context={'message': message})
