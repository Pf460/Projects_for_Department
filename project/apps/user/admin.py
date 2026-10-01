from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('id' ,'email', 'fio', 'is_staff', 'is_active') #list_display - какие колонки показываются в админке
    list_filter = ('email', 'is_staff', 'is_active') #list_filter - фильтрация по колонкам
    search_fields = ('email', 'fio') #search_firlds - поисковая строка, где можно найти строку БД по определённым параметрам
    ordering = ('id',) #ordering - фильтрация по умолчанию

    #Какие поля показываются в админке
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Персональная информация', {'fields': ('fio',)}),
        ('Права', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    readonly_fields = ('last_login',) #Автоматическое изменение, последнего входа user на сайт

    add_fieldsets = (
        (None, {
            'classes': ('wide',), #wide - css-форма для джанго
            'fields': ('email', 'fio', 'password1', 'password2'),
        }),
    )

