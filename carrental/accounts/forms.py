from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput


#Form that changes default registration form into polish
class UserCreateForm(UserCreationForm):

    # username = forms.CharField(max_length=64,label='Nazwa użytkownika',help_text='Maksymalnie 64 litery. Dozwolone litery, liczby oraz @/./+/-/_')
    # email = forms.EmailField(label='Adres e-mail')
    # password1 = forms.CharField(widget=PasswordInput(),label= 'Podaj hasło',help_text='Hasło nie może być podobne do nazwy użytkownika i adresu e-mail''</br>'
    #                                                             'Hasło musi zawierać minimum 8 znaków''</br>'
    #                                                             'Hasło nie może być często wybieranym hasłem np: "abcd1234", "password"''</br>'
    #                                                             'Hasło nie może składać się tylko z cyfr'
    #                             )
    # password2 = forms.CharField(widget=PasswordInput(),label='Powtórz hasło',help_text='Proszę wpisać ponownie hasło celem weryfikacji')


    class Meta:
        model = get_user_model()
        fields = ('username','email','password1','password2')


    def __str__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Adress'

