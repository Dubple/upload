from django import forms
import models

class RegisterForm(forms.ModelForm):
    class Meta:
        model = models.User

        fields = ('first_name', 'last_name', 'username', 'email', 'password')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control signupform-control name', 'id': 'first_name', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control signupform-control name', 'id': 'last_name', 'placeholder': 'Last name'}),
            'username': forms.TextInput(attrs={'class': 'form-control signupform-control', 'id': 'username', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control signupform-control', 'id': 'email', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control signupform-control', 'id': 'pswd', 'placeholder': 'Password'}),
        }

class CstmLoginForm(forms.ModelForm):
    class Meta:
        model = models.User

        fields = ('username', 'password')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control signupform-control', 'id': 'username', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control signupform-control', 'id': 'pswd', 'placeholder': 'Password'}),
        }

class FileUploadForm(forms.ModelForm):

    class Meta:
        model = models.File

        fields = ('file', 'name', 'description')

        widgets = {
            'file': forms.FileInput(attrs={'class': 'form-control upform', 'id': 'upfile'}),
            'name': forms.TextInput(attrs={'class': 'form-control upform', 'id': 'name', 'placeholder': 'file name'}),
            'description': forms.TextInput(attrs={'class': 'form-control upform', 'id': 'description', 'placeholder': 'description'}),
        }
