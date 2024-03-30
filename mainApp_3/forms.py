from django import forms

from mainApp_3.models import *

class MuallifForm(forms.ModelForm):
    class Meta:
        model = Muallif
        fields = ['ism', 'jins', 'tugilgan_sana', 'kitoblar_soni', 'tirik']

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['talaba', 'kitob', 'kutubxonachi', 'qaytardi', 'qaytarish_sana']

class KutubxonachiForm(forms.ModelForm):
    class Meta:
        model = Kutubxonachi
        fields = ['ism', 'ish_vaqti']










