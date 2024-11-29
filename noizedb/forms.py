from django import forms
from .models import Coordinates, Measurement

class MeasurmentForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ('Nlevel','location','MNlevel','From','Chark')
        widgets = {
            'location': forms.HiddenInput()
        }

class NoiseSourcesForm(forms.Form):
    CHOICES = [
        ('2', 'Транспорт'),
        ('3', 'Промышленные зоны'),
        ('4', 'Строящиеся объекты'),
        ('5', 'Магазины'),
        ('6', 'Туристические объекты'),
    ]
    source = forms.ChoiceField(
        label = "Тип источников шума",
        widget=forms.RadioSelect(attrs={
            'display': 'inline-block',
        }),
        choices=CHOICES, 
    )