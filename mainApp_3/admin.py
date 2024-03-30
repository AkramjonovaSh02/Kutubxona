from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, Group

admin.site.register(Talaba)
#admin.site.register(Muallif)
#@admin.register(Muallif)
#class MuallifAdmin(admin.ModelAdmin):
#    list_display = ('ism','jins', 'tugilgan_sana', 'kitoblar_soni', 'tirik', 'id')
#    list_editable = ('tirik', 'kitoblar_soni')
#    list_display_links = ('id', 'ism')
#    search_fields = ('ism', 'id', 'tugilgan_sana')
#    ordering = ('ism', 'tugilgan_sana')
#    date_hierarchy = 'tugilgan_sana'
#    list_per_page = 2

#admin.site.register(Kitob)
@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    list_display = ( 'nom', 'janr', 'sahifa', 'muallif')
    list_editable = ('sahifa', )
#    list_display_links = ('id', 'nom')
    search_fields = ('nom', 'janr')
    autocomplete_fields = ('muallif',)
#1
@admin.register(Kutubxonachi)
class KutubxonachiAdmin(admin.ModelAdmin):
    list_filter = ('ish_vaqti',)
    search_fields = ('ism', )
    search_help_text = ('Ism boyicha qidirissh')
#2
@admin.register(Muallif)
class MualifAdmin(admin.ModelAdmin):
    search_fields = ('ism', )
    search_help_text = ('Ism boyicha qidirissh')
    list_filter = ('tirik', 'jins')
    list_display = ('id', 'ism', 'kitoblar_soni', 'tirik')
    list_display_links = ('id', 'ism')
    list_editable = ('kitoblar_soni', 'tirik')

admin.site.register(Record)




