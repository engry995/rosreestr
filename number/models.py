from django.db import models
from django.db.models import CharField, BooleanField, DateField, FileField, ForeignKey, URLField


class BaseObject(models.Model):

    BUILDING = 'BLD'
    FLAT = 'FLT'

    TYPE_OBJECT_CHOICES = [
        (BUILDING, 'Здание'),
        (FLAT, 'Квартира'),
    ]

    number = CharField(max_length=100, unique=True, null=True, blank=True, verbose_name='кадастровый номер')
    type_object = CharField(max_length=5, choices=TYPE_OBJECT_CHOICES, default=FLAT, verbose_name='тип объекта')
    address = CharField(max_length=300, verbose_name='адрес', blank=True)
    download = BooleanField(verbose_name='паспорт загружен', default=False)
    date_of_download = DateField(verbose_name='дата загрузки паспорта', blank=True, null=True)
    zip = FileField(upload_to='passports/', verbose_name='zip архив', blank=True)
    url = URLField(blank=True, verbose_name='ссылка на файл')
    parent = ForeignKey('self', on_delete=models.PROTECT, blank=True, verbose_name='здание',
                        null=True, limit_choices_to={'type_object': BUILDING})

    def __str__(self):
        return f'{self.number} {self.address[:30]}'

    class Meta:
        verbose_name = 'объект'
        verbose_name_plural = 'объекты'
