from django.contrib import admin
from .models import BaseObject


class ObjectInline(admin.TabularInline):
    model = BaseObject
    fields = ('number', 'address', 'download', 'zip', )
    readonly_fields = ('number', 'address', 'download', 'zip', )
    extra = 0


@admin.register(BaseObject)
class BaseObjectAdmin(admin.ModelAdmin):

    list_display = ('type_object', 'number', 'download', 'count_all_and_download', 'address', 'zip', 'parent')
    list_display_links = ('type_object', 'number',)
    list_editable = ('address',)
    list_filter = ('type_object', 'parent', 'download')
    search_fields = ('number', 'address',)
    inlines = (ObjectInline, )

    @admin.display(description='помещений всего/загружено', empty_value='----')
    def count_all_and_download(self, obj):
        if obj.type_object == BaseObject.BUILDING:
            qs = obj.baseobject_set
            all_passport = qs.count()
            download = qs.filter(download=True).count()

            return f'{all_passport} / {download}'
