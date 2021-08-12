from .models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.',widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.',widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(max_length=254,required=True, help_text='Required. Inform a valid email address.',widget=forms.TextInput(attrs={'class': "form-control"}))
    phone = forms.CharField(required=True,max_length=20)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','phone', 'password1', 'password2', )

    def __init__(self, *args, **kwargs):
       super(SignUpForm, self).__init__(*args, **kwargs)
       for key in self.fields:
           self.fields[key].widget.attrs['class'] = 'form-control'


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].widget.attrs['class'] = 'form-control'


class ProfileForm(forms.ModelForm): 
    long_desc = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta: 
        model = Profile 
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(ProfileForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(ProfileForm, self).save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance