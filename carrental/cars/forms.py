from .models import Car, CarDetail, CarMain, Comment
from django.forms import ModelForm, DateInput
from django import forms
from django.core.validators import MinValueValidator

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['main', 'detail']


class CarDetailForm(ModelForm):
    production_date_start = forms.DateField(widget=DateInput(
                format=('%d/%m/%Y'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date',}
            ))
    production_date_end = forms.DateField(widget=DateInput(
                format=('%d/%m/%Y'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date',}
            ))
    power_min = forms.IntegerField(min_value=0)
    power_max = forms.IntegerField(min_value=0)
    price_min = forms.DecimalField(max_digits=9, decimal_places=2, validators=[MinValueValidator(0.00)])
    price_max = forms.DecimalField(max_digits=9, decimal_places=2, validators=[MinValueValidator(0.00)])
    check_in =  forms.DateField(widget=DateInput(
                format=('%d/%m/%Y'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date',}
            ))
    check_out =  forms.DateField(widget=DateInput(
                format=('%d/%m/%Y'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date',}
            ))
    class Meta:
        model = CarDetail
        exclude = ('car', 'power', 'production_date', 'price')


    def __init__(self, *args, **kwargs):
        super(CarDetailForm, self).__init__(*args, **kwargs)
        self.fields['color'].required = False
        self.fields['seats'].required = False
        self.fields['fuel'].required = False
        self.fields['production_date_end'].required = False
        self.fields['production_date_start'].required = False
        self.fields['power_min'].required = False
        self.fields['power_max'].required = False
        self.fields['price_min'].required = False
        self.fields['price_max'].required = False
        self.fields['check_in'].required = False
        self.fields['check_out'].required = False


class CarMainForm(ModelForm):
    class Meta:
        model = CarMain
        exclude = ('car', )

    def __init__(self, *args, **kwargs):
        super(CarMainForm, self).__init__(*args, **kwargs)
        self.fields['model'].required = False
        self.fields['marka'].required = False

class AvailabilityForm(forms.Form):
    check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
        }